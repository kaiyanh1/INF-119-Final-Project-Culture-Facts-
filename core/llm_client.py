# Author: Your Name - Student ID: XXXXXXX

import os
import google.generativeai as genai
from core.usage_tracker import usage_tracker

# Initialize Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


class LLMClient:
    """
    Wrapper for Gemini API.
    """

    def __init__(self, model_name, agent_name):
        self.model_name = model_name
        self.agent_name = agent_name
        self.model = genai.GenerativeModel(model_name)

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        """
        Send prompt to Gemini and return output text.
        """
        response = self.model.generate_content(
            [
                {"role": "system", "parts": system_prompt},
                {"role": "user", "parts": user_prompt},
            ]
        )

        text = response.text

        usage_tracker.record(self.agent_name, len(text.split()))

        return text
