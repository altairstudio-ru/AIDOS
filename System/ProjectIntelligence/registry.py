import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROJECTS_DIR = os.path.join(BASE_DIR, "Projects")


def list_projects():
    return [
        d for d in os.listdir(PROJECTS_DIR)
        if os.path.isdir(os.path.join(PROJECTS_DIR, d))
    ]


def score_project(task_text: str, project_name: str) -> int:
    """
    MVP scoring (replace with embeddings later)
    """

    text = task_text.lower()
    name = project_name.lower()

    score = 0

    # direct match
    if name in text:
        score += 50

    # keyword overlap
    for word in text.split():
        if word in name:
            score += 10

    return score


def select_project(task_text: str) -> str:
    projects = list_projects()

    best_project = None
    best_score = 0

    for project in projects:
        score = score_project(task_text, project)

        if score > best_score:
            best_score = score
            best_project = project

    # threshold
    if best_score < 20:
        return "Auto-Generated-Project"

    return best_project or "Auto-Generated-Project"
