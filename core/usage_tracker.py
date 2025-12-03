# Author: Your Name - Student ID: XXXXXXX

class UsageTracker:
    """
    Tracks how many times each agent calls a model
    and how many tokens they used in total.
    """

    def __init__(self):
        self.data = {}

    def record(self, agent_name: str, total_tokens: int):
        if agent_name not in self.data:
            self.data[agent_name] = {"numApiCalls": 0, "totalTokens": 0}
        self.data[agent_name]["numApiCalls"] += 1
        self.data[agent_name]["totalTokens"] += total_tokens

    def get_usage_report(self):
        return self.data


# Global singleton usage tracker
usage_tracker = UsageTracker()
