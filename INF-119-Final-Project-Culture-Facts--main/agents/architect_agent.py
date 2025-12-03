# Author: Youssef Dessouky - Student ID: 92158941
"""
Architect agent is for designing prompt for culture facts, 
and then generating the content of main.py, culture_service.py, data/cultures.json
"""

import json
import re
from core.llm_client import LLMClient

ARCHITECT_SYSTEM_PROMPT = """
You are the Architect Agent in a multi-agent MCP system.
You must generate the full code files for a Culture Facts Python app.

Requirements:
1. Terminal UI with a menu system
2. JSON data file with at least 5 different cultures
3. Functions required in culture_service.py:
   - list_cultures(): returns list of all culture names
   - search_culture(name): searches for a culture by name (case-insensitive)
   - get_random_fact(): returns a random cultural trivia tidbit
   - get_details(culture_name): returns detailed info about a specific culture
4. main.py must be runnable: python main.py
5. data/cultures.json must contain at least 5 cultures with these fields for each:
   - name: string
   - region: string
   - description: string
   - facts: list of strings (at least 3 facts per culture)
   - traditions: list of strings

Important coding guidelines:
- Use proper imports (json, random, os)
- Handle file paths correctly using os.path
- Include error handling for file not found
- The JSON file path should be relative to culture_service.py location

Respond ONLY with valid JSON in this exact format (no markdown, no extra text):
{
  "files": {
    "main.py": "<full python code for main.py>",
    "culture_service.py": "<full python code for culture_service.py>",
    "data/cultures.json": "<full json content>"
  }
}
"""


class ArchitectAgent:
    """
    Uses the LLM to produce a full file plan plus initial code
    for the Culture Facts application.
    """

    def __init__(self, model_name="gemini-2.0-flash"):
        self.llm = LLMClient(model_name, "architect_agent")
      
    def analyze_requirements(self, requirements):
        """
        Ask the LLM to generate a JSON design + code.
        """
        prompt = f"""User requirements:
{requirements}

Generate the complete Culture Facts application now. Remember:
1. main.py should have a menu loop with options to: list cultures, search, random fact, get details, quit
2. culture_service.py should load data from data/cultures.json
3. data/cultures.json should have at least 5 diverse cultures with rich data

Return ONLY the JSON structure, no markdown code blocks."""

        raw = self.llm.ask(ARCHITECT_SYSTEM_PROMPT, prompt)

        # Try to parse JSON
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            # Clean up the response - remove markdown code blocks if present
            cleaned = raw
            # Remove ```json and ``` markers
            cleaned = re.sub(r'^```json\s*', '', cleaned, flags=re.MULTILINE)
            cleaned = re.sub(r'^```\s*$', '', cleaned, flags=re.MULTILINE)
            cleaned = cleaned.strip()
            
            try:
                return json.loads(cleaned)
            except json.JSONDecodeError as e:
                # If still failing, try to extract JSON from the response
                json_match = re.search(r'\{[\s\S]*\}', cleaned)
                if json_match:
                    return json.loads(json_match.group())
                raise ValueError(f"Failed to parse architect response: {e}\nRaw: {raw[:500]}")
