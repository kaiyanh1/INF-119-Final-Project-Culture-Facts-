# Author: Your Name - Student ID: XXXXXXX

from mcp_server.server import MCPServer

def main():
    server = MCPServer()
    res = server.call_tool("run_pytest")
    print(res["stdout"])
    print(res["stderr"])

if __name__ == "__main__":
    main()
