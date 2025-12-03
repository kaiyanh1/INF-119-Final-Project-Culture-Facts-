# Author: Your Name - Student ID: XXXXXXX

from mcp_server.server import MCPServer
from core.usage_tracker import usage_tracker

class CoderAgent:
    """
    Takes the Architect's file plan and writes files to disk
    using the MCP server tools.
    """

    def __init__(self, mcp_server: MCPServer):
        self.server = mcp_server
        self.name = "coder_agent"

    def generate_code(self, plan: dict):
        """
        plan is expected to have a "files" dict: { path: content }.
        """
        files = plan.get("files", {})
        # CoderAgent does not call LLM, but you can add "check/repair" logic to it.
        # Here, we simply call the tool to write files.
        for path, content in files.items():
            self.server.call_tool("write_file", path=path, content=content)

        # This is a record of "virtual tokens" to include this agent in the usage report.        usage_tracker.record(self.name, 1)
        return {"status": "code_written", "num_files": len(files)}
