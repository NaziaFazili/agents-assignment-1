"""
Task Definitions for Research Crew

TODO: Define the four sequential tasks:
1. Query Expansion - Break down the research question
2. Source Hunting - Search the paper corpus
3. Synthesis - Analyze and synthesize findings
4. Report Writing - Generate the literature review

Each task should:
- Have a clear description telling the agent what to do
- Specify the agent responsible
- Define expected_output format
- Use context parameter to pass information between tasks
"""

from agents import query_expander, report_writer, source_hunter, synthesizer
from crewai import Task


def create_research_tasks(research_question: str) -> list[Task]:
    """
    Create the task pipeline for a research question.

    Args:
        research_question: The user's research question

    Returns:
        List of 4 tasks in execution order

    Implement the four tasks below
    """

    # =========================================
    # Task 1: Query Expansion
    # =========================================
    # Create a task that breaks down the research question
    # into sub-questions, keywords, and search angles
    #
    expand_task = Task(
        description=f"Analyze the research question: {research_question}. "
        "Break it into focused sub-questions, keywords, "
        "and different perspective for searching same question",
        agent=query_expander,
        expected_output=(
            "A structured list containing:\n"
            " 4 focused sub-questions\n"
            " Important keywords and concepts\n"
            " 4 useful search queries"
        ),
    )

    # =========================================
    # Task 2: Source Hunting
    # =========================================
    # Create a task that searches the paper corpus
    # Hint: Use context=[expand_task] to pass the query strategy
    #
    search_task = Task(
        description="Use the expanded queries to search the paper corpus. "
        "Find 8-12 relevant passages using the search_papers tool. "
        "Search more than once if needed, and include the source paper for each passage.",
        agent=source_hunter,
        context=[expand_task],
        expected_output=(
            "A collection of 8-12 relevant passages. For each passage include:\n"
            " The passage\n"
            " The source title\n"
            " Why the passage is relevant to the research question"
        ),
    )

    # =========================================
    # Task 3: Synthesis
    # =========================================
    # Create a task that synthesizes findings into themes
    # Hint: Use context=[expand_task, search_task] for full context
    #
    synthesis_task = Task(
        description=(
            "Review the evidence from the papers. "
            "Identify the main themes, agreements, disagreements, and research gaps. "
            "Use only the retrieved evidence."
        ),
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output="  A structured research synthesis containing:\n"
        " Major themes found across the sources\n"
        " Agreements between papers\n"
        " Disagreements or different approaches\n"
        " Research gaps or unanswered questions\n"
        " Source references supporting each major finding",
    )

    # =========================================
    # Task 4: Report Writing
    # =========================================
    # Create a task that writes the final literature review
    # Hint: Use context=[expand_task, search_task, synthesis_task]
    #
    report_task = Task(
        description=(
            "Write a clear review using the retrieved evidence and synthesis. "
            "Use proper citations and only include supported information. "
            "Write the report in Markdown format."
        ),
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        expected_output=(
            "A Markdown literature review with these sections:\n"
            "1. Executive Summary\n"
            "2. Introduction\n"
            "3. Methodology\n"
            "4. Findings\n"
            "5. Discussion\n"
            "6. Conclusion\n"
            "7. References\n"
            "Organize the findings by theme and cite the source papers."
        ),
    )

    # Return your tasks in order
    return [expand_task, search_task, synthesis_task, report_task]

    # Placeholder - replace with your implementation
    raise NotImplementedError(
        " Implement create_research_tasks() in tasks/task_definitions.py"
    )
