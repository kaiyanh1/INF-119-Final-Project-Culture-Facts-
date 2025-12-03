# Author: Your Name - Student ID: XXXXXXX

from core.orchestrator import Orchestrator

def run_system(requirements):
    orch = Orchestrator(model_name="gemini-1.5-flash")
    result = orch.build_app(requirements)
    usage = orch.server.call_tool("get_usage")

    return {"result": result, "usage": usage}
