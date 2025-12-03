"""Starter Code"""
# Author: (Your Name) - Student ID: XXXXXXX

from mcp_server.tools import write_file, read_file, get_usage

class MCPServer:
    def __init__(self):
        self.tools = {
            "write_file": write_file,
            "read_file": read_file,
            "get_usage": get_usage
        }

    def call_tool(self, tool_name, **kwargs):
        if tool_name not in self.tools:
            return {"error": "Tool not found"}
        return self.tools[tool_name](**kwargs)

