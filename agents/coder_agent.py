"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

from core.usage_tracker import usage_tracker

class CoderAgent:

    def __init__(self, model, mcp_server):
        self.model = model
        self.server = mcp_server
        self.name = "coder_agent"

    def generate_code(self, plan):
        """Convert the architect plan into actual Python code."""
        
        usage_tracker.record(self.name, 300)

        for path, content in plan["files"].items():
            self.server.call_tool("write_file", path=path, content=content)

        return {"status": "code_generated"}

