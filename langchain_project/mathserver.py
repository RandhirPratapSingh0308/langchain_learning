from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math")
@mcp.tool()
def add(a:int,b:int) -> int:
    """
    adds two numbers
    """
    return a+b

@mcp.tool()
def sub(a:float,b:float) -> float:
    """
    subtracts two numbers
    """
    return a-b

@mcp.tool()
def multiple(a:int,b:int) -> int:
    """
    multiplies two numbers
    """
    return a*b


# The transport="stdio" argumnets tells the server to:

# Use standerd input/output (stdin & stdout) to recive and respond to tool function calls.multiple

if __name__ == "__main__":
    mcp.run(transport="stdio")