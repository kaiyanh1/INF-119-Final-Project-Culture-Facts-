"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

from core.usage_tracker import usage_tracker

class TesterAgent:

    def __init__(self, model, mcp_server):
        self.model = model
        self.server = mcp_server
        self.name = "tester_agent"

    def generate_tests(self):
        """
        Use the LLM to generate at least 10 test cases.
        """

        usage_tracker.record(self.name, 200)

        test_code = """
def test_placeholder():
    assert True
"""
        self.server.call_tool("write_file", path="tests/test_sample.py", content=test_code)

        return {"status": "tests_generated"}

