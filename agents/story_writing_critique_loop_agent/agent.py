from google.adk.agents import SequentialAgent, LoopAgent
from .sub_agents.draft_writer import draft_writer_agent
from .sub_agents.critic import critic_agent
from .sub_agents.writer import refiner_agent

# The LoopAgent contains the agents that will run repeatedly: Critic -> Refiner.
story_refinement_loop = LoopAgent(
    name="StoryRefinementLoop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=3, # Prevents infinite loops
)

# The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.
root_agent = SequentialAgent(
    name="StoryPipeline",
    sub_agents=[draft_writer_agent, story_refinement_loop],
)
