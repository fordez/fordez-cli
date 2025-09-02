from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    google,
    cartesia,
    deepgram,
    silero,
    noise_cancellation,
)

from livekit.plugins.turn_detector.multilingual import MultilingualModel

from google.genai.types import Modality
from google.genai import types

load_dotenv(".env.local")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""Instrucciones para el Agente de Ventas de Gas
        1. Presentación

        Saluda al cliente con amabilidad.
        Ejemplo:

        “¡Hola! Soy tu asesor de gas domiciliario, ¿en qué te puedo ayudar hoy?”

        2. Identificación de la necesidad

        Pregunta al cliente qué tipo de gas o qué cantidad necesita.
        Ejemplo:

        “¿Qué marca de gas deseas recargar hoy?”
        o
        “¿Buscas el precio más económico, el gas más duradero o el de mejor rendimiento?”

        3. Ofertas disponibles

        Explica las marcas y precios claramente:

        Montagas → 80.000 COP (la opción más económica).

        Gaspais → 90.000 COP (balance entre precio y calidad).

        Supergar → 100.000 COP (mayor duración y rendimiento).

        4. Persuasión ligera

        Orienta al cliente según sus preferencias:

        Si busca ahorro → Recomendar Montagas.

        Si quiere equilibrio precio/calidad → Recomendar Gaspais.Si busca más rendimiento → Recomendar Supergar""")


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.5-flash-live-preview",
            modalities=[Modality.TEXT],
            temperature=0.8,
            realtime_input_config=types.RealtimeInputConfig(
                  automatic_activity_detection=types.AutomaticActivityDetection(
                     disabled=True,
                  ),
            ),
            input_audio_transcription=None,
        ),

        stt = deepgram.STT(
              model="nova-3",
              language="multi"
        ),
        tts=cartesia.TTS(
              model="sonic-2",
              voice="b042270c-d46f-4d4f-8fb0-7dd7c5fe5615",
        )
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` instead for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions="Hola como estas en que te puedo ayudar"
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
