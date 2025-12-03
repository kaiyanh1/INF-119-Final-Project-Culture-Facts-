This project implements a complete **multi-agent system** using **Google Gemini** and a custom **MCP (Model Context Protocol) server** to automatically generate:

- The full Culture Facts application code (15-20 cultures)
- At least 10 pytest test cases (≥ 8 tests must pass)
- A model usage tracking report
- A GUI for input and execution

The system satisfies all project requirements:
- Multi-agent design
- MCP integration (file I/O, test runner, usage tracking)
- GUI input
- Automatic code generation
- Automatic test generation
- Usage tracking JSON
- Fully runnable by following the instructions in this README

---

# 1. Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
flask
pytest
google-generativeai>=0.5.0
```

---

# 2. Set Your Gemini API Key

The system uses **Gemini 1.5 Flash**.

### macOS / Linux:
```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

### Windows PowerShell:
```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

---

# 3. Project Structure

```
ai-coder-culture-facts/
│
├── mcp_server/
│   ├── server.py
│   ├── tools.py
│
├── agents/
│   ├── architect_agent.py
│   ├── coder_agent.py
│   ├── tester_agent.py
│
├── core/
│   ├── orchestrator.py
│   ├── usage_tracker.py
│   ├── llm_client.py
│
├── gui/
│   ├── app.py
│
├── generated_app/         # Output auto-generated here
│
├── run_system.py
├── run_tests.py
└── requirements.txt
```

All generated files (main.py, culture_service.py, tests, JSON data) will be placed inside `generated_app/`.

---

# 4. How to Run

1. Clone the repository and install dependencies (see sections 1-2 above)
2. Set your Gemini API key (see section 2)
3. Start the GUI:
   ```bash
   python gui/app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser
5. Paste Culture Facts requirements and click **Generate App**

The system runs 3 agents:
- **Architect Agent** → Generates full code plan (JSON with 15-20 cultures)
- **Coder Agent** → Writes files into `generated_app/` via MCP
- **Tester Agent** → Generates ≥10 pytest tests via MCP

The GUI displays generated files, test results, and usage tracking JSON.

---

# 5. Running Generated Tests

```bash
python run_test.py
```

OR manually:

```bash
cd generated_app
pytest
```

Expected: At least 10 tests with ≥8 passing.

---

# 6. MCP Server Tools

Our custom MCP server exposes the following tools:

| Tool | Description |
|------|-------------|
| `write_file` | Writes code into `generated_app/<path>` |
| `read_file` | Reads generated files |
| `run_pytest` | Executes pytest inside `generated_app` |
| `get_usage` | Returns model usage stats |

Agents do **not** perform file I/O directly — they must call MCP tools, fulfilling the MCP requirement.

---

# 7. Multi-Agent System Architecture

| Agent | Model | Responsibilities |
|--------|-------------|----------------|
| **ArchitectAgent** | gemini-1.5-flash | Generates complete file contents in a JSON spec (main.py, culture_service.py, cultures.json with 15-20 cultures) |
| **CoderAgent** | gemini-1.5-flash | Uses MCP `write_file` tool to write files to disk |
| **TesterAgent** | gemini-1.5-flash | Generates ≥10 pytest test cases and writes them via MCP |

Agents communicate only through MCP tools. This satisfies the assignment's multi-agent + MCP communication requirements.

---

# 8. Model Usage Tracking

We track number of API calls and total estimated tokens per agent. Data appears in the GUI after every build as JSON. Tracking is implemented in `usage_tracker.py`.

---

# 9. Output Location

The generated Culture Facts application appears in `generated_app/`:
- `main.py` - Terminal UI application
- `culture_service.py` - Core service functions
- `data/cultures.json` - Culture data (15-20 cultures)
- `tests/test_culture_service.py` - Pytest test suite

Run the app:
```bash
cd generated_app
python main.py
```
