"""
Report Writer Agent

TODO: Implement this agent that produces a well-structured literature
review with proper citations.

Hints:
- Define a role focused on academic writing and communication
- Set a goal to produce a clear, well-organized literature review
- Write a backstory emphasizing clarity and proper attribution
- The output should be in markdown with sections:
  1. Executive Summary
  2. Introduction
  3. Methodology
  4. Findings (organized by theme)
  5. Discussion
  6. Conclusion
  7. References
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

report_writer = Agent(
    role="Report writer",
    goal="Write a clear and well organized in a predefined format, using the synthesized research findings and attributing them to correct source",
    backstory=(
        "You are an experienced writer skilled at turning research findings "
        "into clear, well organized literature reviews. All claims are "
        "supported by the appropriate sources and citations."
    ),
    tools=[],
    verbose=True,
    memory=True,
)
