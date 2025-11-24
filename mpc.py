from crewai import Agent

agent = Agent(
    role="Research Analyst",
    goal="Research and analyze information",
    backstory="Expert researcher with access to external tools",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key",           # External MCP server
        "https://api.weather.com/mcp#get_forecast",          # Specific tool from server
        "crewai-amp:financial-data",                         # CrewAI AMP marketplace
        "crewai-amp:research-tools#pubmed_search"            # Specific AMP tool
    ]
)
# MCP tools are now automatically available to your agent!
