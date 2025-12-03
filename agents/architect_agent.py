# Author: Your Name - Student ID: XXXXXXX
"""
Architect agent is for designing prompt for cluture facts, 
and then generating the content of main.py,culture_service.py, data/cultures.json
""""
import json
from core.llm_client import LLMClient

ARCHITECT_SYSTEM_PROMPT = """
You are the Architect Agent in a multi-agent MCP coding system.

You design a small Python console application called "Culture Facts".

The app requirements:
- Show a list of cultures/countries.
- Show detailed information for a selected culture.
- Provide a random cultural fact.
- Allow searching cultures by name.
- Use a simple text-based (terminal) UI.
- Use a static JSON file as data source.
- The code must be runnable with: `python main.py` inside the generated_app folder.

You MUST output a complete JSON object with this exact schema:

{
  "files": {
    "main.py": "<full Python source code>",
    "culture_service.py": "<full Python source code>",
    "data/cultures.json": "<valid JSON array with culture data>"
  }
}

Rules:
- Use standard Python only (no external libraries except json and random).
- Do not include comments like "TODO".
- The generated code must be runnable without modifications.
- For cultures.json, include at least 5 different cultures and 2 facts each.
- Respond ONLY with the JSON. No explanations, no extra text.
"""


class ArchitectAgent:
    """
    Uses the LLM to produce a full file plan plus initial code
    for the Culture Facts application.
    """

    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.llm = LLMClient(model_name, agent_name="architect_agent")

    def analyze_requirements(self, requirements: str) -> dict:
        """
        Ask the LLM to generate a JSON design + code.
        Here we mostly ignore the free-form requirements and trust the system prompt,
        but you can also append the user requirements.
        """
        user_prompt = f"""
User requirements (for reference):

{requirements}

Now generate the JSON object with the files as specified.
"""
        raw = self.llm.ask(ARCHITECT_SYSTEM_PROMPT, user_prompt)

        # Try to parse JSON
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            # simple fallback：if it has ```json ，delelte it
            cleaned = raw.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.strip("`")
                # remove "json\n"
                cleaned = cleaned.replace("json\n", "").replace("json\r\n", "")
            data = json.loads(cleaned)

        return data
