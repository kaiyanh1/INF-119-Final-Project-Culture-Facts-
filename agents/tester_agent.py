# Author: Your Name - Student ID: XXXXXXX

import json
from core.llm_client import LLMClient

TESTER_SYSTEM_PROMPT = """
You are the Tester Agent.
Generate at least 10 pytest tests for Culture Facts app.

Respond ONLY in JSON:
{
  "files": {
    "tests/test_culture_service.py": "..."
  }
}
"""

class TesterAgent:
    """
    Uses the LLM to generate pytest test files for the Culture Facts app.
    """
  
    def __init__(self, mcp_server, model_name="gemini-1.5-flash"):
        self.server = mcp_server
        self.llm = LLMClient(model_name, "tester_agent")

    def generate_tests(self):
        """
        Ask the LLM to produce a JSON with test files and write them to generated_app.
        """
        user_prompt = "Generate tests now."
        raw = self.llm.ask(TESTER_SYSTEM_PROMPT, "Generate tests now.")

        try:
            data = json.loads(raw)
        except:
            cleaned = raw.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned)

        for path, content in data["files"].items():
            self.server.call_tool("write_file", path=path, content=content)

        return {"status": "tests_written"}
