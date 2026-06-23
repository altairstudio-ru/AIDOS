import os
from datetime import datetime


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def create_task(project_path, idx, title, desc, agent="coder"):
    tasks_dir = f"{project_path}/Tasks"
    ensure_dir(tasks_dir)

    task_id = f"TASK-{idx:03d}"
    path = f"{tasks_dir}/{task_id}.md"

    content = f"""# {task_id}

## Title
{title}

## Agent
{agent}

## Description
{desc}

## Status
TODO

## Created
{datetime.now().isoformat()}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path


def generate_tasks(project_path, plan_text):
    """
    простой стабильный парсер без LLM
    """

    mapping = [
        ("Download Service", "Implement file download logic"),
        ("Storage Manager", "Implement file storage system"),
        ("Queue System", "Implement task queue"),
        ("Auth System", "Implement authentication"),
        ("API Wrapper", "Wrap external API"),
        ("QA System", "Testing and validation")
    ]

    created = []

    for i, (title, desc) in enumerate(mapping, 1):
        path = create_task(project_path, i, title, desc)
        created.append(path)

    return created
