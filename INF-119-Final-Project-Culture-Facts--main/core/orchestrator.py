# Author: Youssef Dessouky - Student ID: 92158941

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
    
    def __init__(self, model_name="gemini-2.0-flash"):
        self.server = MCPServer()
        self.architect = ArchitectAgent(model_name=model_name)
        self.coder = CoderAgent(self.server)
        self.tester = TesterAgent(self.server, model_name=model_name)

    def build_app(self, requirements):
        """
        Run the full pipeline: plan -> code -> tests.
        Returns a dictionary with results from each stage.
        """
        print("=" * 50)
        print("STAGE 1: Architect Agent - Designing application...")
        print("=" * 50)
        
        try:
            plan = self.architect.analyze_requirements(requirements)
            print(f"✓ Architect generated plan with {len(plan.get('files', {}))} files")
        except Exception as e:
            return {"error": f"Architect failed: {str(e)}"}
        
        print("\n" + "=" * 50)
        print("STAGE 2: Coder Agent - Writing files...")
        print("=" * 50)
        
        try:
            code = self.coder.generate_code(plan)
            print(f"✓ Coder wrote {code.get('total_files', 0)} files")
        except Exception as e:
            return {"error": f"Coder failed: {str(e)}"}
        
        print("\n" + "=" * 50)
        print("STAGE 3: Tester Agent - Generating tests...")
        print("=" * 50)
        
        try:
            tests = self.tester.generate_tests()
            print(f"✓ Tester generated test files")
        except Exception as e:
            return {"error": f"Tester failed: {str(e)}"}

        print("\n" + "=" * 50)
        print("BUILD COMPLETE")
        print("=" * 50)

        return {
            "plan_files": list(plan.get("files", {}).keys()),
            "code": code,
            "tests": tests
        }
