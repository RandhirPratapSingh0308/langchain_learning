from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Returns the weather for a given location.
    """
    return f"The weather in {location} is 25 degree celcius and 30 kph wind speed."

if __name__ == "__main__":
    mcp.run(transport="stdio")
