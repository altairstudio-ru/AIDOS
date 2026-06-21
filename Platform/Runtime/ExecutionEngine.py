import os
import datetime

def update_task_status(task_path, status):
    with open(task_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "Status" in content:
        content = content.split("Status")[0] + f"Status\n{status}\n\n" + content.split("Status")[1]

    with open(task_path, "w", encoding="utf-8") as f:
        f.write(content)


def append_log(task_path, message):
    timestamp = datetime.datetime.now().isoformat()

    with open(task_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n# Log [{timestamp}]\n{message}\n")


def execute_task(task_path, agent_name="Executive"):
    update_task_status(task_path, "in_progress")

    append_log(task_path, f"Assigned to agent: {agent_name}")

    # здесь позже будет вызов LLM / агентов
    result = f"Task executed by {agent_name} (mock result)"

    append_log(task_path, result)

    update_task_status(task_path, "done")

    return result
