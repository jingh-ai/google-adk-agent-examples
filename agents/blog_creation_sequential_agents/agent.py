from google.adk.agents import SequentialAgent
from .sub_agents.outliner import outline_agent
from .sub_agents.writer import writer_agent
from .sub_agents.editor import editor_agent

# Root Agent: Manages the sequence of sub-agents to create a complete blog post.
root_agent = SequentialAgent(
    name="BlogPipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent],
)
