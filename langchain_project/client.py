import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv(find_dotenv())

# Determine path to server files
CURRENT_DIR = Path(__file__).resolve().parent
MATH_SERVER = str(CURRENT_DIR / "mathserver.py")
WEATHER_SERVER = str(CURRENT_DIR / "weather.py")

async def main():
    # Pass current environment so subprocesses inherit the virtualenv
    server_env = dict(os.environ)

    client = MultiServerMCPClient(
        {
            "math": {
                "command": sys.executable,
                "args": [MATH_SERVER],
                "transport": "stdio",
                "env": server_env,
            },
            "weather": {
                "command": sys.executable,
                "args": [WEATHER_SERVER],
                "transport": "stdio",
                "env": server_env,
            },
        }
    )

    tools = await client.get_tools()
    print("Available Tools:", [tool.name for tool in tools])

    model = ChatGroq(model="qwen/qwen3.8-27b")
    agent = create_react_agent(model, tools)

    # 1. Math query
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is 15 multiplied by 12, and what is 100 minus 42?"}]}
    )
    print("\nMath Response:")
    print(math_response["messages"][-1].content)

    # 2. Weather query
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in Cairo?"}]}
    )
    print("\nWeather Response:")
    print(weather_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
