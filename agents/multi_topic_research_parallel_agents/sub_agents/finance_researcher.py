# Finance Researcher: Focuses on fintech trends.
from google.adk.agents import Agent
from google.adk.tools import google_search


finance_research_agent = Agent(
    name="FinanceResearcher",
    model="gemini-2.5-flash-lite",
    instruction="""Research current fintech trends. Include 3 key trends,
their market implications, and the future outlook. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="finance_research", # The result will be stored with this key.
)
