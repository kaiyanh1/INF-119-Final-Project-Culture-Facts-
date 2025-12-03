# Author: Your Name - Student ID: XXXXXXX

from agents.architect_agent import ArchitectAgent
from agents.coder_agent import CoderAgent
from agents.tester_agent import TesterAgent
from mcp_server.server import MCPServer

class Orchestrator:
    """
    Orchestrates the multi-agent workflow:
    - ArchitectAgent: design + generate code plan
    - CoderAgent: write code files
    - TesterAgent: generate tests
    """
    
    def __init__(self, model_name="gemini-1.5-flash"):
        self.server = MCPServer()
        self.architect = ArchitectAgent(model_name=model_name)
        self.coder = CoderAgent(self.server)
        self.tester = TesterAgent(self.server, model_name=model_name)

    def build_app(self, requirements):
        """
        Run the full pipeline: plan -> code -> tests.
        """
        plan = self.architect.analyze_requirements(requirements)
        code = self.coder.generate_code(plan)
        tests = self.tester.generate_tests()

        return {
            "plan_files": list(plan["files"].keys()),
            "code": code,
            "tests": tests
        }
