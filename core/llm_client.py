import openai
from core.usage_tracker import usage_tracker

class LLMClient:

    def __init__(self, model_name, agent_name):
        self.model = model_name
        self.agent_name = agent_name

    def ask(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        tokens = response.usage.total_tokens
        usage_tracker.record(self.agent_name, tokens)

        return response.choices[0].message["content"]

