"""
Synthesizer Agent

TODO: Implement this agent that analyzes collected sources to identify
themes, agreements, contradictions, and gaps in the literature.

Hints:
- Define a role focused on synthesis and analysis
- Set a goal to identify themes, consensus, debates, and gaps
- Write a backstory emphasizing pattern recognition across sources
- This agent primarily reasons - may not need tools
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

# TODO: Create the synthesizer agent
#
synthesizer = Agent(
    role="Synthesiser and Analyzer",
    goal="Analyze evidence from different papers and synthesize it into themes, agreements, disagreements, and research gaps",
    backstory="You are skilled in comparing information from multiple academic sources and synthesize them. You identify common themes, agreements, disagreements, and gaps in the research. ",
    tools=[],
    verbose=True,
    memory=True,
)
