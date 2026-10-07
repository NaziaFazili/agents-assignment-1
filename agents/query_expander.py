"""
Query Expander Agent

TODO: Implement this agent that transforms a broad research question
into a comprehensive search strategy with sub-questions, keywords,
and search angles.

Hints:
- Define a clear role (e.g., "Research Query Strategist")
- Set a goal focused on breaking down questions and identifying keywords
- Write a backstory that gives the agent expertise in research methodology
- Consider what tools might help (keyword extraction, synonym generation)
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

query_expander = Agent(
    role="Query Expander",
    goal="Take the original research question and break it into focused sub-questions and useful keywords",
    backstory=(
        "You are an expert research assistant who specializes in breaking research questions "
        "into clear shorter sub-questions and keywords."
    ),
    tools=[],
    verbose=True,
    memory=True,
)
