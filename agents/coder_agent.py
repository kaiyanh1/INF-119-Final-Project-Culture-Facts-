"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

import json

class CoderAgent:

    def __init__(self, model, mcp_server, name="coder_agent"):
        self.llm = LLMClient(model, name)
        self.server = mcp_server

    def generate_code(self, plan):
        files = plan["files"]

        for path, content in files.items():
            self.server.call_tool("write_file", path=path, content=content)

        return {"status": "code_written"}

