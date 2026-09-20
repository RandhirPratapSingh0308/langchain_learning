# LangChain Learning

A repository for learning and experimenting with LangChain, LangGraph, agents, tools, and integrations.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RandhirPratapSingh0308/langchain_learning.git
   cd langchain_learning
   ```

2. **Set up the virtual environment:**
   ```bash
   uv sync
   # or with pip:
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Copy the example environment file and populate your API keys:
   ```bash
   cp .env.example .env
   ```
   Add your keys in `.env`:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## Project Structure
- `langchain_project/1-langchainintro.ipynb`: Introduction to LangChain concepts.
- `langchain_project/2-tools.ipynb`: Using and binding tools with LangChain.
- `langchain_project/3-agentintro.ipynb`: Basic Agent architectures.
- `langchain_project/4-agentmultitools.ipynb`: Multi-tool Agents.