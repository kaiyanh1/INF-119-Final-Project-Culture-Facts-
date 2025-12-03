"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

from mcp_server.server import MCPServer
from agents.architect_agent import ArchitectAgent
from agents.coder_agent import CoderAgent
from agents.tester_agent import TesterAgent
from core.orchestrator import Orchestrator

def run_system(requirements):
    server = MCPServer()

    architect = ArchitectAgent(model="fake-llm")
    coder = CoderAgent(model="fake-llm", mcp_server=server)
    tester = TesterAgent(model="fake-llm", mcp_server=server)

    orchestrator = Orchestrator(architect, coder, tester)

    result = orchestrator.build_app(requirements)

    usage = server.call_tool("get_usage")
    return {
        "result": result,
        "usage": usage
    }
