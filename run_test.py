# Author: Your Name - Student ID: XXXXXXX

from mcp_server.server import MCPServer

def main():
    """Run pytest from generated_app via command line"""
    server = MCPServer()
    result = server.call_tool("run_pytest")
    print("Return code:", result["returncode"])
    print("=== STDOUT ===")
    print(result["stdout"])
    print("=== STDERR ===")
    print(result["stderr"])

if __name__ == "__main__":
    main()

