"""
Source Hunter Agent

TODO: Implement this agent that searches the curated paper corpus
to find relevant passages for each sub-question in the query strategy.

Hints:
- This agent MUST use the search_papers tool from tools.paper_rag_tool
- Define a role focused on investigation and source discovery
- Set a goal to find 8-12 relevant passages
- Write a backstory emphasizing thoroughness and not stopping at first results
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent
from tools.paper_rag_tool import search_papers

# TODO: Create the source_hunter agent
#
source_hunter = Agent(
    role="Source Hunter",
    goal=(
        "Find 8-12 relevant evidence for the topic from the provided paper corpus, "
        " and also include the source for each evidence."
    ),
    backstory=(
        "You are a thorough academic assistant and specialize in finding relevant acadmic evidence from the provided research papers. "
        "You need to search for 8-12 relevant evidences. These evidences should fully support the research question. "
    ),
    tools=[search_papers],  # This tool is required!
    verbose=True,
    memory=True,
)
