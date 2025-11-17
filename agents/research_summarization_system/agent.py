from google.adk.agents import Agent
from google.adk.tools import AgentTool
from .sub_agents.research_specialist import research_agent
from .sub_agents.summary_specialist import summarizer_agent


# Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
research_coordinator_agent = Agent(
    name="ResearchCoordinator",
    model="gemini-2.5-flash-lite",
    # This instruction tells the root agent HOW to use its tools (which are the other agents).
    instruction="""You are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.
1. First, you MUST call the `ResearchAgent` tool to find relevant information on the topic provided by the user.
2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` tool to create a concise summary.
3. Finally, present the final summary clearly to the user as your response.""",
    # We wrap the sub-agents in `AgentTool` to make them callable tools for the root agent.
    tools=[
        AgentTool(research_agent),
        AgentTool(summarizer_agent)
    ],
)

root_agent = research_coordinator_agent

