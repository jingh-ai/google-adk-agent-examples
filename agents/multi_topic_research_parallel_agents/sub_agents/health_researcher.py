# Health Researcher: Focuses on medical breakthroughs.
from google.adk.agents import Agent
from google.adk.tools import google_search


health_research_agent = Agent(
    name="HealthResearcher",
    model="gemini-2.5-flash-lite",
    instruction="""Research recent medical breakthroughs. Include 3 significant advances,
their practical applications, and estimated timelines. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="health_research", # The result will be stored with this key.
)
