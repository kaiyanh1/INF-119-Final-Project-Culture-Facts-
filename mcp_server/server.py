# Author: Your Name - Student ID: XXXXXXX

from mcp_server.tools import write_file, read_file, run_pytest, get_usage

class MCPServer:
    """
    Minimal MCP-like server that exposes tools as a dictionary.
    In a real MCP implementation, this would speak the MCP protocol.
    """

    def __init__(self):
        self.tools = {
            "write_file": write_file,
            "read_file": read_file,
            "run_pytest": run_pytest,
            "get_usage": get_usage,
        }

    def call_tool(self, tool_name: str, **kwargs):
        """
        Call a registered tool by name.
        """
        if tool_name not in self.tools:
            return {"error": f"Tool {tool_name} not found"}
        return self.tools[tool_name](**kwargs)
