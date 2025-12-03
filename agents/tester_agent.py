# Author: Your Name - Student ID: XXXXXXX

import json
from core.llm_client import LLMClient
from mcp_server.server import MCPServer

TESTER_SYSTEM_PROMPT = """
You are the Tester Agent in a multi-agent MCP system.

The project is a Python console app "Culture Facts" with files:
- main.py
- culture_service.py
- data/cultures.json

Your job:
- Generate AT LEAST 10 pytest test cases.
- Put them into a single file named tests/test_culture_service.py.
- At least 8 tests should pass if the implementation is correct.
- Tests should import functions from culture_service.py.
- The tests should check:
  - list_cultures returns a non-empty list
  - get_random_fact returns a string
  - search_culture returns relevant results for existing cultures
  - get_details returns full info for valid input and None for invalid

Output format must be exactly:

{
  "files": {
    "tests/test_culture_service.py": "<full test file content>"
  }
}

Rules:
- Use pytest style (functions starting with test_).
- Import the functions you need from culture_service.
- Respond ONLY with the JSON. No extra text.
"""


class TesterAgent:
    """
    Uses the LLM to generate pytest test files for the Culture Facts app.
    """

    def __init__(self, mcp_server: MCPServer, model_name: str = "gpt-4o-mini"):
        self.server = mcp_server
        self.llm = LLMClient(model_name, agent_name="tester_agent")

    def generate_tests(self) -> dict:
        """
        Ask the LLM to produce a JSON with test files and write them to generated_app.
        """
        user_prompt = "Generate tests now."
        raw = self.llm.ask(TESTER_SYSTEM_PROMPT, user_prompt)

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            cleaned = raw.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.strip("`")
                cleaned = cleaned.replace("json\n", "").replace("json\r\n", "")
            data = json.loads(cleaned)

        files = data.get("files", {})
        for path, content in files.items():
            self.server.call_tool("write_file", path=path, content=content)

        return {"status": "tests_written", "num_files": len(files)}
