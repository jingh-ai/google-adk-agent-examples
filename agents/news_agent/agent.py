from google.adk.agents import ParallelAgent, SequentialAgent
from .sub_agents.aggregator import aggregator_agent
from .sub_agents.worker_google_news import google_agent
from .sub_agents.worker_dds import duckduckgo_agent
from .sub_agents.editor import editor_agent


# The ParallelAgent runs all its sub-agents simultaneously.
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[google_agent, duckduckgo_agent],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
# The root_agent can now be executed to perform the entire multi-topic research and aggregation process.
root_agent = SequentialAgent(
    name="NewsSystem",
    sub_agents=[parallel_research_team, aggregator_agent, editor_agent],
)