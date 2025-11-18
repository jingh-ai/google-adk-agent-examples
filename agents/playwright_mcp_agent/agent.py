from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .tools.mcp_tools import mcp_playwright_server


root_agent = LlmAgent(
    name="playwright_automator_agent",
    model="gemini-2.5-flash-lite",
    #description="An agent that can perform web page data scraping.",
    instruction=(
        "You are an expert web automation agent. "
        "You can navigate to web pages, take screenshots, fill forms, and click elements. "
        "When asked to interact with a web page, use the appropriate browser tools. "
        "If you don't know something, you can always google it using the browser tools"
    ),
    tools=[mcp_playwright_server]
    )

