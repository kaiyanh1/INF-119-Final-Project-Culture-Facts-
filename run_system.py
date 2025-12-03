# Author: Your Name - Student ID: XXXXXXX

from core.orchestrator import Orchestrator
from mcp_server.server import MCPServer

def run_system(requirements: str):
    """
    High-level entry point for running the whole system from GUI.
    """
    orchestrator = Orchestrator(model_name="gpt-4o-mini")
    result = orchestrator.build_app(requirements)

    # After build, we want to get usage report from MCP tools
    server = orchestrator.server
    usage = server.call_tool("get_usage")

    return {
        "build": result,
        "usage": usage,
    }
