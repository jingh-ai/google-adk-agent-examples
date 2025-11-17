from google.adk.agents import ParallelAgent, SequentialAgent
from .sub_agents.tech_researcher import tech_research_agent 
from .sub_agents.health_researcher import health_research_agent
from .sub_agents.finance_researcher import finance_research_agent 
from .sub_agents.aggregator import aggregator_agent


# The ParallelAgent runs all its sub-agents simultaneously.
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[tech_research_agent, health_research_agent, finance_research_agent],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
# The root_agent can now be executed to perform the entire multi-topic research and aggregation process.
root_agent = SequentialAgent(
    name="ResearchSystem",
    sub_agents=[parallel_research_team, aggregator_agent],
)
