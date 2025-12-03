"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

class Orchestrator:

    def __init__(self, architect, coder, tester):
        self.architect = architect
        self.coder = coder
        self.tester = tester

    def build_app(self, requirements):
        plan = self.architect.analyze_requirements(requirements)

        self.coder.generate_code(plan)

        self.tester.generate_tests()

        return {"status": "build_complete"}
