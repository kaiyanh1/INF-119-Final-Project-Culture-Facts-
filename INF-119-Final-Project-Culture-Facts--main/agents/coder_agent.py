# Author: Youssef Dessouky - Student ID: 92158941

from core.usage_tracker import usage_tracker


class CoderAgent:
    """
    Takes the Architect's file plan and writes files to disk
    using the MCP server tools.
    """
    
    def __init__(self, mcp_server):
        self.server = mcp_server
        self.name = "coder_agent"

    def generate_code(self, plan):
        """
        plan is expected to have a "files" dict: { path: content }.
        Writes each file using the MCP server's write_file tool.
        """
        files = plan.get("files", {})
        written_files = []

        for path, content in files.items():
            result = self.server.call_tool("write_file", path=path, content=content)
            if result.get("status") == "ok":
                written_files.append(path)
            else:
                print(f"Warning: Failed to write {path}: {result}")

        # Record usage - CoderAgent doesn't call LLM but we track its activity
        usage_tracker.record(self.name, len(written_files))
        
        return {
            "status": "code_written",
            "files_written": written_files,
            "total_files": len(written_files)
        }
