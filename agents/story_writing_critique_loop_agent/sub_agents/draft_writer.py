# This agent runs ONCE at the beginning to create the first draft.
from google.adk.agents import Agent


draft_writer_agent = Agent(
    name="DraftWriterAgent",
    model="gemini-2.5-flash-lite",
    instruction="""Based on the user's prompt, write the first draft of a short story (around 100-150 words).
    Output only the story text, with no introduction or explanation.""",
    output_key="current_story", # Stores the first draft in the state.
)

