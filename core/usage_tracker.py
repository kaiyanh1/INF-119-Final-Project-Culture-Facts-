"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

class UsageTracker:
    def __init__(self):
        self.data = {}

    def record(self, agent_name, tokens):
        if agent_name not in self.data:
            self.data[agent_name] = {"numApiCalls": 0, "totalTokens": 0}
        self.data[agent_name]["numApiCalls"] += 1
        self.data[agent_name]["totalTokens"] += tokens

    def get_usage_report(self):
        return self.data


usage_tracker = UsageTracker()
