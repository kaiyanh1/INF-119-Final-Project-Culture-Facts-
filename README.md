This project implements a complete **multi-agent system** using **Google Gemini** and a custom **MCP (Model Context Protocol) server** to automatically generate:

- The full Culture Facts application code  
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

# 4. How to Run the Program (TA Instructions)

These steps are **all the TA needs** to run the entire system.

---

## STEP 1 — Clone Repository

```bash
git clone <YOUR_REPO_URL>
cd ai-coder-culture-facts
```

---

## STEP 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## STEP 3 — Set Gemini API Key

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

Windows:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

---

## STEP 4 — Start GUI

```bash
python gui/app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## STEP 5 — Generate the Culture Facts Application

Inside the GUI:

1. Paste the Culture Facts requirements (any text or language).
2. Click **Generate App**.
3. The system will run all 3 agents:
   - **Architect Agent** → Generates full code plan (JSON)
   - **Coder Agent** → Writes files into `generated_app/`
   - **Tester Agent** → Generates ≥10 pytest tests
4. The GUI will show:
   - Generated file list
   - Test generation result
   - Model usage tracking JSON

Example output in browser:

```
{
  "result": {
    "plan_files": [...],
    "code": {...},
    "tests": {...}
  },
  "usage": {
    "architect_agent": {...},
    "coder_agent": {...},
    "tester_agent": {...}
  }
}
```

---

# 5. Running the Generated Tests

After generating the app, run:

```bash
python run_tests.py
```

OR manually:

```bash
cd generated_app
pytest
```

You will see:

- At least 10 tests
- At least 8 passing tests (required by assignment)

---

# 6. MCP Server Tools (Important for Grading)

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
| **ArchitectAgent** | gemini-1.5-flash | Generates complete file contents in a JSON spec (main.py, culture_service.py, JSON data) |
| **CoderAgent** | gemini-1.5-flash | Uses MCP `write_file` tool to write files to disk |
| **TesterAgent** | gemini-1.5-flash | Generates ≥10 pytest test cases and writes them via MCP |

Agents communicate only through MCP tools.  
This satisfies the assignment’s multi-agent + MCP communication requirements.

---

# 8. Model Usage Tracking

We track:

- Number of API calls per agent  
- Total estimated tokens per agent  

Data appears in the GUI after every build:

```
{
  "architect_agent": { "numApiCalls": X, "totalTokens": Y },
  "coder_agent": { "numApiCalls": X, "totalTokens": Y },
  "tester_agent": { "numApiCalls": X, "totalTokens": Y }
}
```

Tracking is implemented in `usage_tracker.py`.

---

# 9. Output Location

The generated Culture Facts application will appear inside:

```
generated_app/
    main.py
    culture_service.py
    data/cultures.json
    tests/test_culture_service.py
```

The TA can run the app directly:

```bash
cd generated_app
python main.py
```

---

# 10. Summary

This system provides:

- Multi-agent architecture (Architect, Coder, Tester)
- Gemini LLM integration
- Custom MCP server with tools
- GUI interface
- Automatic code generation
- Automatic test generation
- Usage tracking
- Fully runnable output application


