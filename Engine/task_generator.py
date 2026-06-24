from datetime import datetime
from Engine.config import tasks_path


def create_task(project_name, idx, title, desc, agent="coder"):
    base = tasks_path(project_name)
    base.mkdir(parents=True, exist_ok=True)

    task_id = f"TASK-{idx:03d}"
    path = base / f"{task_id}.md"

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

    path.write_text(content, encoding="utf-8")
    return str(path)


def generate_tasks(project_name, plan_text):
    mapping = [
        ("Download Service", "Implement file download logic"),
        ("Storage Manager", "Implement file storage system"),
        ("Queue System", "Implement task queue"),
        ("Auth System", "Implement authentication"),
        ("API Wrapper", "Wrap external API"),
        ("QA System", "Testing and validation")
    ]

    result = []

    for i, (title, desc) in enumerate(mapping, 1):
        result.append(create_task(project_name, i, title, desc))

    return result