from typing import List
from app.models.task import Task

# Toggle this later for real LLM
USE_AI_STUB = True


def generate_daily_plan(tasks: List[Task]):
    """
    Generate a daily plan for a user based on their tasks.
    """

    if USE_AI_STUB:
        return {
            "daily_plan": [
                "Focus on completing in-progress tasks first.",
                "Start one high-priority TODO task.",
                "Review completed tasks and prepare next steps."
            ]
        }

    # --- Future real LLM integration ---
    # Placeholder for real AI call
    return {
        "daily_plan": [
            "AI integration not implemented yet."
        ]
    }