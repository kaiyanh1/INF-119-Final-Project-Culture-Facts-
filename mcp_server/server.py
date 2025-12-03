"""Starter Code"""
# Author: (Your Name) - Student ID: XXXXXXX

from tools import write_file, read_file, run_tests, get_usage

class MCPServer:
    """
    Minimal MCP server skeleton.
    You will add tool registration and communication protocol here.
    """

    def __init__(self):
        self.tools = {
            "write_file": write_file,
            "read_file": read_file,
            "run_tests": run_tests,
            "get_usage": get_usage
        }

    def call_tool(self, tool_name, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name](**kwargs)
        else:
            return {"error": f"Tool {tool_name} not found"}
