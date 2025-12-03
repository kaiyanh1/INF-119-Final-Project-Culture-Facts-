"""Starter code"""
# Author: (Your Name) - Student ID: XXXXXXX

class TesterAgent:

    def __init__(self, model, mcp_server, name="tester_agent"):
        self.llm = LLMClient(model, name)
        self.server = mcp_server

    def generate_tests(self, structure_summary):
        prompt = open("prompts/tester_prompt.txt").read()
        prompt = prompt.replace("<<< GENERATED_CODE_STRUCTURE >>>", structure_summary)

        result = self.llm.ask(prompt)
        test_files = json.loads(result)["files"]

        for path, content in test_files.items():
            self.server.call_tool("write_file", path=path, content=content)

        return {"status": "tests_written"}
