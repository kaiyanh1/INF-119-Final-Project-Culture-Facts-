# AI Coder - Culture Facts Multi-Agent System

This project implements a complete **multi-agent system** using **Google Gemini** and a custom **MCP (Model Context Protocol) server** to automatically generate a Culture Facts application.

## Features Generated

- **Culture Facts Application** with Terminal UI
- **At least 10 pytest test cases** (≥ 8 tests must pass)
- **Model usage tracking report**
- **Flask GUI** for input and execution

## Project Requirements Satisfied

- ✅ Multi-agent design (Architect, Coder, Tester)
- ✅ MCP integration (file I/O, test runner, usage tracking)
- ✅ GUI input (Flask web interface)
- ✅ Automatic code generation
- ✅ Automatic test generation
- ✅ Usage tracking JSON
- ✅ Fully runnable output

---

## 1. Requirements

### Python Version
- Python 3.11 (recommended)

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Set Your Gemini API Key

The system uses **Gemini 2.0 Flash**.

### macOS / Linux:
```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

### Windows PowerShell:
```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

### Windows Command Prompt:
```cmd
set GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## 3. Project Structure

```
INF-119-Final-Project-Culture-Facts--main/
│
├── agents/
│   ├── __init__.py
│   ├── architect_agent.py    # Generates code design
│   ├── coder_agent.py        # Writes files via MCP
│   └── tester_agent.py       # Generates pytest tests
│
├── core/
│   ├── __init__.py
│   ├── llm_client.py         # Gemini API wrapper
│   ├── orchestrator.py       # Coordinates agents
│   └── usage_tracker.py      # Tracks API usage
│
├── gui/
│   ├── __init__.py
│   └── app.py                # Flask web interface
│
├── mcp_server/
│   ├── __init__.py
│   ├── server.py             # MCP server implementation
│   └── tools.py              # MCP tools (file I/O, pytest)
│
├── generated_app/            # Output directory (auto-generated)
│   ├── main.py
│   ├── culture_service.py
│   ├── data/cultures.json
│   └── tests/test_culture_service.py
│
├── run_system.py             # Main system entry point
├── run_test.py               # Test runner
├── requirements.txt
└── README.md
```

---

## 4. How to Run (TA Instructions)

### STEP 1 — Install Dependencies

```bash
cd INF-119-Final-Project-Culture-Facts--main
pip install -r requirements.txt
```

### STEP 2 — Set API Key

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

### STEP 3 — Start the GUI

```bash
python gui/app.py
```

Open your browser at: **http://127.0.0.1:5000**

### STEP 4 — Generate the Application

1. Enter your requirements in the text area (or use the default)
2. Click **"Generate Culture Facts App"**
3. Wait 30-60 seconds for the agents to complete
4. View the results showing:
   - Generated files list
   - Test generation status
   - Model usage statistics

---

## 5. Running the Generated Application

After generation, run the Culture Facts app:

```bash
cd generated_app
python main.py
```

---

## 6. Running the Tests

```bash
python run_test.py
```

Or manually:

```bash
cd generated_app
pytest -v
```

Expected: At least 10 tests, with ≥ 8 passing.

---

## 7. MCP Server Tools

| Tool | Description |
|------|-------------|
| `write_file` | Writes code to `generated_app/<path>` |
| `read_file` | Reads files from generated_app |
| `run_pytest` | Executes pytest in generated_app |
| `get_usage` | Returns model usage statistics |

---

## 8. Multi-Agent Architecture

| Agent | Model | Responsibilities |
|-------|-------|------------------|
| **ArchitectAgent** | gemini-2.0-flash | Designs app structure, generates all code in JSON |
| **CoderAgent** | N/A (uses MCP) | Writes files to disk via MCP tools |
| **TesterAgent** | gemini-2.0-flash | Generates ≥10 pytest test cases |

---

## 9. Usage Tracking

After each build, usage statistics are displayed:

```json
{
  "architect_agent": { "numApiCalls": 1, "totalTokens": 2500 },
  "coder_agent": { "numApiCalls": 1, "totalTokens": 3 },
  "tester_agent": { "numApiCalls": 1, "totalTokens": 1500 }
}
```

---

## 10. Troubleshooting

### API Key Error
Make sure the environment variable is set correctly:
```bash
echo $GEMINI_API_KEY  # Should show your key
```

### Import Errors
Run from the project root directory:
```bash
cd INF-119-Final-Project-Culture-Facts--main
python gui/app.py
```

### Test Failures
If tests fail, you can regenerate or manually check `generated_app/` files.

---

## Author

Your Name - Student ID: XXXXXXX
