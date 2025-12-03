"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

import json
from core.llm_client import LLMClient

class ArchitectAgent:

    def __init__(self, model="gpt-4o", name="architect_agent"):
        self.llm = LLMClient(model, name)

    def analyze_requirements(self, requirements):
        prompt = open("prompts/architect_prompt.txt").read()
        prompt = prompt.replace("<<< USER_REQUIREMENTS >>>", requirements)

        result = self.llm.ask(prompt)
        return json.loads(result)
