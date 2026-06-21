import os
from datetime import datetime
from language import normalize
from router import route
from System.ProjectIntelligence.registry import select_project


# =========================
# BASE PATH (stable root)
# =========================

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECTS_DIR = os.path.join(BASE_DIR, "Projects")


# =========================
# PROJECT RESOLUTION
# =========================

def get_project_path(project_name: str) -> str:
    return os.path.join(PROJECTS_DIR, project_name)


# =========================
# TASK CREATION ENGINE
# =========================

def create_task(project_path: str, task_text: str, role: str) -> str:
    tasks_dir = os.path.join(project_path, "Tasks")
    os.makedirs(tasks_dir, exist_ok=True)

    task_id = f"TASK-{int(datetime.now().timestamp())}"
    task_file = os.path.join(tasks_dir, f"{task_id}.md")

    content = f"""# Task

## ID
{task_id}

## Title
{task_text}

## Assigned Role
{role}

## Status
Pending

## Created At
{datetime.now().isoformat()}
"""

    with open(task_file, "w", encoding="utf-8") as f:
        f.write(content)

    return task_file


# =========================
# SCI CORE PIPELINE
# =========================

def process_science_command(raw_input: str):
    """
    Core SCI pipeline:
    input → normalize → project → role → task → file
    """

    if not raw_input.strip():
        return {
            "error": "Empty input"
        }

    # 1. Language normalization (RU/EN → system format)
    normalized = normalize(raw_input)

    # 2. Project Intelligence Layer (semantic routing)
    project_name = select_project(normalized)
    project_path = get_project_path(project_name)

    # 3. Role routing
    role = route(normalized)

    # 4. Task creation
    task_file = create_task(project_path, normalized, role)

    # 5. System response
    return {
        "project": project_name,
        "role": role,
        "task_file": task_file,
        "status": "created"
    }


# =========================
# CLI ENTRY (for now)
# =========================

def main():
    print("\nSCI READY")
    print("Enter command:\n")

    user_input = input("> ")

    result = process_science_command(user_input)

    print("\nSYSTEM OUTPUT")
    for k, v in result.items():
        print(f"{k}: {v}")


# =========================
# FUTURE UI / API READY
# =========================

def run_sci_api(input_text: str):
    """
    This function will be used later by:
    - FastAPI backend
    - Web UI
    - Telegram bot
    """
    return process_science_command(input_text)


if __name__ == "__main__":
    main()
