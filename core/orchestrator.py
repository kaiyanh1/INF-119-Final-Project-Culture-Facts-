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

    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.server = MCPServer()
        self.architect = ArchitectAgent(model_name=model_name)
        self.coder = CoderAgent(self.server)
        self.tester = TesterAgent(self.server, model_name=model_name)

    def build_app(self, requirements: str) -> dict:
        """
        Run the full pipeline: plan -> code -> tests.
        """
        plan = self.architect.analyze_requirements(requirements)
        code_result = self.coder.generate_code(plan)
        test_result = self.tester.generate_tests()

        return {
            "plan_files": list(plan.get("files", {}).keys()),
            "code_result": code_result,
            "test_result": test_result,
        }
