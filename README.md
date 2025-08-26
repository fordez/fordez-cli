
# Fordez-cli

**fordez-cli** is a command-line tool for programming AI-driven tasks through the creation and orchestration of AI agents integrated with **MCP (Model Context Protocol) servers**.

This CLI enables you to connect agents with specialized tools, making workflows dynamic, modular, and extensible.

---

## 🚀 Features

* Create and orchestrate AI agents.
* Connect to MCP servers for enhanced task execution.
* Modular design for easy extension.
* Efficient workflow automation with AI-powered logic.

---

## 📦 Integrated MCP Servers

### 1. **Everything**

Reference/test server providing prompts, resources, and tools.

**Example Prompt:**

```
Agent: "What is the capital of France?"
```

**Result:**

```
Paris
```

---

### 2. **Fetch**

Fetches and converts web content for efficient LLM usage.

**Example Prompt:**

```
Agent: "Fetch the latest news from https://example.com/news"
```

**Result:**

```
[Article Title] Breaking News: Example Headline
[Summary] The article reports on...
```

---

### 3. **Filesystem**

Secure file operations with configurable access controls.

**Example Prompt:**

```
Agent: "List all files in ./data"
```

**Result:**

```
data/
 ├── report1.txt
 ├── dataset.csv
 └── summary.md
```

---

### 4. **Git**

Tools to read, search, and manipulate Git repositories.

**Example Prompt:**

```
Agent: "Get the last 3 commits from the repo"
```

**Result:**

```
1. [abc123] Fix bug in data pipeline
2. [def456] Add README documentation
3. [ghi789] Initial commit
```

---

### 5. **Memory**

Persistent memory system powered by a knowledge graph.

**Example Prompt:**

```
Agent: "Remember that John's favorite color is blue"
Agent: "What is John's favorite color?"
```

**Result:**

```
Blue
```

---

### 6. **Sequential Thinking**

Dynamic and reflective problem-solving through step-by-step reasoning.

**Example Prompt:**

```
Agent: "Plan steps to cook pasta"
```

**Result:**

```
1. Boil water
2. Add pasta
3. Cook for 10 minutes
4. Drain water
5. Serve with sauce
```

---

### 7. **Time**

Time and timezone conversion capabilities.

**Example Prompt:**

```
Agent: "Convert 3 PM EST to PST"
```

**Result:**

```
12 PM PST
```

---

## 🛠️ Installation

```bash
git clone https://github.com/fordez/fordez-cli.git
cd fordez-cli
pip install -r requirements.txt
```

---

## ⚡ Usage

```bash
python fordez.py
```

Then interact with the CLI to create agents and connect them with MCP servers.

---

## 🔮 Roadmap

* Add more MCP servers (Google Sheets, Salesforce, HubSpot).
* Extend orchestration logic for multi-agent workflows.
* Add voice input/output capabilities.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📄 License

MIT License.

---

👉 Do you want me to also add a **usage demo section** (like a step-by-step CLI session example showing agent creation + connecting with one MCP server)? That would make the README feel even more practical.
