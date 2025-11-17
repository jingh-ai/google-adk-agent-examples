# Research Agent: Its job is to use the google_search tool and present findings.
from google.adk.agents import Agent
from google.adk.tools import google_search


research_agent = Agent(
    name="ResearchAgent",
    model="gemini-2.5-flash-lite",
    instruction="You are a specialized research agent. Your only job is to use the google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.",
    tools=[google_search],
    output_key="research_findings", # The result of this agent will be stored in the session state with this key.
)

