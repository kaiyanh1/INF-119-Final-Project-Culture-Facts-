# Author: Your Name - Student ID: XXXXXXX

import os
from openai import OpenAI
from core.usage_tracker import usage_tracker

# Create a single shared OpenAI client
_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

class LLMClient:
    """
    Simple wrapper around OpenAI chat.completions API
    that also records token usage.
    """

    def __init__(self, model_name: str, agent_name: str):
        self.model_name = model_name
        self.agent_name = agent_name

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        """
        Send a prompt to the model and return the text content.
        """
        response = _client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
        )

        # Record token usage
        if response.usage is not None:
            total_tokens = response.usage.total_tokens
        else:
            total_tokens = 0

        usage_tracker.record(self.agent_name, total_tokens)

        content = response.choices[0].message.content
        return content
