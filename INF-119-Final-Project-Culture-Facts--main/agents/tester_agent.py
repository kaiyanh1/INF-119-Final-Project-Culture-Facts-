# Author: Youssef Dessouky - Student ID: 92158941

import json
import re
from core.llm_client import LLMClient

TESTER_SYSTEM_PROMPT = """
You are the Tester Agent in a multi-agent system.
Generate comprehensive pytest tests for a Culture Facts application.

The application has these components:
1. culture_service.py with functions:
   - list_cultures(): returns list of culture names
   - search_culture(name): searches cultures by name (case-insensitive)
   - get_random_fact(): returns a random fact string
   - get_details(culture_name): returns dict with culture details
   
2. data/cultures.json: JSON file with culture data

Generate AT LEAST 10 pytest test functions that test:
- list_cultures returns a non-empty list
- list_cultures returns correct type (list)
- search_culture finds existing cultures
- search_culture handles case-insensitive search
- search_culture returns None or empty for non-existent culture
- get_random_fact returns a string
- get_random_fact returns non-empty result
- get_details returns correct data structure
- get_details handles non-existent culture gracefully
- Integration test: all cultures from list can be retrieved with get_details

Important:
- Import from culture_service (it's in the same directory level)
- Use proper pytest assertions
- Include docstrings for each test
- Make tests independent of each other

Respond ONLY with valid JSON (no markdown):
{
  "files": {
    "tests/test_culture_service.py": "<full pytest code>"
  }
}
"""


class TesterAgent:
    """
    Uses the LLM to generate pytest test files for the Culture Facts app.
    """
  
    def __init__(self, mcp_server, model_name="gemini-2.0-flash"):
        self.server = mcp_server
        self.llm = LLMClient(model_name, "tester_agent")

    def generate_tests(self):
        """
        Ask the LLM to produce a JSON with test files and write them to generated_app.
        """
        user_prompt = """Generate at least 10 comprehensive pytest tests now.
        
Make sure tests cover:
1. Test list_cultures returns list
2. Test list_cultures is not empty
3. Test list_cultures contains strings
4. Test search_culture finds valid culture
5. Test search_culture case insensitive
6. Test search_culture returns None for invalid
7. Test get_random_fact returns string
8. Test get_random_fact is not empty
9. Test get_details returns dict
10. Test get_details has required keys
11. Test get_details for invalid culture
12. Test integration - all listed cultures have details

Return ONLY JSON, no markdown code blocks."""

        raw = self.llm.ask(TESTER_SYSTEM_PROMPT, user_prompt)

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            # Clean up markdown formatting
            cleaned = raw
            cleaned = re.sub(r'^```json\s*', '', cleaned, flags=re.MULTILINE)
            cleaned = re.sub(r'^```\s*$', '', cleaned, flags=re.MULTILINE)
            cleaned = cleaned.strip()
            
            try:
                data = json.loads(cleaned)
            except json.JSONDecodeError:
                # Try to extract JSON
                json_match = re.search(r'\{[\s\S]*\}', cleaned)
                if json_match:
                    data = json.loads(json_match.group())
                else:
                    raise ValueError(f"Failed to parse tester response: {raw[:500]}")

        # Write test files using MCP tool
        written_files = []
        for path, content in data.get("files", {}).items():
            result = self.server.call_tool("write_file", path=path, content=content)
            if result.get("status") == "ok":
                written_files.append(path)

        return {
            "status": "tests_written",
            "files_written": written_files
        }
