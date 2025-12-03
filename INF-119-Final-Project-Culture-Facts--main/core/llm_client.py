# Author: Youssef Dessouky - Student ID: 92158941

import os
from google import genai
from core.usage_tracker import usage_tracker

# Global client instance
_client = None


def get_client():
    """Get or create the GenAI client."""
    global _client
    if _client is None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            _client = genai.Client(api_key=api_key)
        else:
            _client = genai.Client()  # Will try to get from env automatically
    return _client


class LLMClient:
    """
    Wrapper for Google GenAI API (new SDK).
    """

    def __init__(self, model_name, agent_name):
        self.model_name = model_name
        self.agent_name = agent_name
        self.client = get_client()

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        """
        Send prompt to Gemini and return output text.
        Combines system and user prompts for the request.
        """
        # Combine system prompt with user prompt
        combined_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        # Use the new genai SDK format
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=combined_prompt
        )

        text = response.text

        # Estimate tokens (rough approximation: ~4 chars per token)
        estimated_tokens = len(text) // 4 + len(combined_prompt) // 4
        usage_tracker.record(self.agent_name, estimated_tokens)

        return text
