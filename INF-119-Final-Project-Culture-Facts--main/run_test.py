# Author: Youssef Dessouky - Student ID: 92158941

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp_server.server import MCPServer


def main():
    """
    Run pytest on the generated application.
    """
    server = MCPServer()
    
    print("Running pytest on generated_app...")
    print("-" * 50)
    
    res = server.call_tool("run_pytest")
    
    print("\nSTDOUT:")
    print(res.get("stdout", ""))
    
    if res.get("stderr"):
        print("\nSTDERR:")
        print(res["stderr"])
    
    print("-" * 50)
    print(f"Return code: {res.get('returncode', 'N/A')}")
    
    return res.get("returncode", 1)


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
