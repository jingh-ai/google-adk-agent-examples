from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash-lite",
    description="An agent that can perform Google searches to answer questions.",
    instruction="You are an agent that can perform Google searches to find information and answer questions.",
    tools=[google_search]
    )