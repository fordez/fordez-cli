# Fordez + Uv — Proyecto Completo (librería, YAML e Inferencia)

Este repositorio contiene la librería **Fordez**, lista para instalar con **uv**, empaquetada con:
- Servidor MCP basado en FastAPI (opcional con `fastmcp`).
- Agente interactivo con FastAgent (opcional con `mcp-agent` o `fast-agent-mcp`).
- Configuración centralizada en **YAML** (`config/fordez.yaml`).
- Scripts de entrada (entry points) listos para ejecutar.

---

## 📁 Estructura del repositorio

```
fordez-uv/
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── config/
│   └── fordez.yaml
├── src/
│   └── fordez/
│       ├── __init__.py
│       ├── config.py
│       ├── mcp.py
│       ├── tools.py
│       ├── agent.py
│       └── agent_client.py
├── tests/
│   └── test_basic.py
└── docker/
    ├── Dockerfile
    └── docker-compose.yml
```

---

## 🚀 Instalación

```bash
# Instalar librería en modo editable
task run python -m pip install -e .

# Agregar dependencias opcionales
uv add fastmcp          # Para servidor MCP
uv add mcp-agent rich   # Para agente interactivo
uv add fast-agent-mcp   # Para cliente LLM
```

---

## ▶️ Ejecución

### Servidor MCP
```bash
# Usando script entrypoint
uv run fordez-mcp

# O con uvicorn directamente
uv run uvicorn fordez.tools:app --reload --port 8000
```

### Agente interactivo
```bash
uv run fordez-agent
```

### Cliente que consume tools
```bash
uv run python -m fordez.agent_client
```

---

## ⚙️ Configuración YAML

Archivo: `config/fordez.yaml`

Ejemplo:
```yaml
default_model: gemini2

logger:
  level: "info"
  progress_display: true
  show_chat: true
  show_tools: true

mcp:
  servers:
    fetch:
      command: "uvx"
      args: ["mcp-server-fetch"]
```

📌 Variables como `${DB_PASSWORD}` se expanden desde el entorno.

---

## 🐳 Docker

Construir imagen:
```bash
docker build -t fordez .
```

Levantar con docker-compose:
```bash
docker-compose up --build
```

---

## ✅ Checklist

- [ ] `uv run python -m pip install -e .` funciona.
- [ ] `uv run fordez-mcp` abre `/health` → `{ "status": "ok" }`.
- [ ] `uv run fordez-agent` inicia modo interactivo.
- [ ] `GET /config` devuelve configuración redactada.

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

---

💡 Puedes usar este repositorio como **base para GitHub/GitLab** y extenderlo con CI/CD (GitHub Actions), Kubernetes o Dapr según tus necesidades.

