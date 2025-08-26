from fastmcp import FastMCP

mcp = FastMCP("Demo-Fordez")

@mcp.tool
def add(a:int, b:int)-> int:
    """suma dos numeros"""
    return a + b

if __name__ == "__main__":
    mcp.run()
