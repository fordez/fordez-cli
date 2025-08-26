import asyncio
from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("AgenteSimple")

@fast.agent(
    name="Fordez",
    instruction="Eres un agentes de desarrollo de tareas impulsado por inteligencia artificial",
    servers=["fetch","filesystem","git"]   # aquí le decimos que use solo el servidor 'fetch'
)
async def fordez_agent():
    async with fast.run() as agent:
          await agent.interactive()

if __name__ == "__main__":
    asyncio.run(fordez_agent())
