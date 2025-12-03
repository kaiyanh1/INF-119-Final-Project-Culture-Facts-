# Author: Youssef Dessouky - Student ID: 92158941

class UsageTracker:
    """
    Tracks how many times each agent calls a model
    and how many tokens they used in total.
    """

    def __init__(self):
        self.data = {}

    def record(self, agent_name, tokens):
        if agent_name not in self.data:
            self.data[agent_name] = {"numApiCalls": 0, "totalTokens": 0}
        self.data[agent_name]["numApiCalls"] += 1
        self.data[agent_name]["totalTokens"] += tokens

    def get_usage_report(self):
        return self.data

    def reset(self):
        """Reset all usage data."""
        self.data = {}


# Global singleton instance
usage_tracker = UsageTracker()
