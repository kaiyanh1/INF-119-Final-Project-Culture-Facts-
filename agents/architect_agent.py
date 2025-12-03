# Author: Your Name - Student ID: XXXXXXX
"""
Architect agent is for designing prompt for cluture facts, 
and then generating the content of main.py,culture_service.py, data/cultures.json
""""

import json
from core.llm_client import LLMClient

ARCHITECT_SYSTEM_PROMPT = """
You are the Architect Agent in a multi-agent MCP system.
You must generate the full code files for a Culture Facts Python app.

Requirements:
- Terminal UI
- JSON data file
- Functions: list_cultures, search_culture, get_random_fact, get_details
- main.py must run: python main.py
- data file must contain at least 5 cultures
- Respond ONLY in JSON:
{
  "files": {
    "main.py": "...",
    "culture_service.py": "...",
    "data/cultures.json": "..."
  }
}
"""


class ArchitectAgent:
    """
    Uses the LLM to produce a full file plan plus initial code
    for the Culture Facts application.
    """

    def __init__(self, model_name="gemini-1.5-flash"):
        self.llm = LLMClient(model_name, "architect_agent")
      
    def analyze_requirements(self, requirements):
        """
        Ask the LLM to generate a JSON design + code.
        Here we mostly ignore the free-form requirements and trust the system prompt,
        but you can also append the user requirements.
        """
        prompt = f"User requirements:\n{requirements}\nGenerate the JSON structure now."
        raw = self.llm.ask(ARCHITECT_SYSTEM_PROMPT, prompt)

        # Try to parse JSON
        try:
            return json.loads(raw)
        except:
            cleaned = raw.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned)
