import os
from Engine.executor import call_model
from Engine.model_map import MODEL_MAP
from Engine.config import tasks_path


def run_task_file(task_file, project_name):
    with open(task_file, "r", encoding="utf-8") as f:
        task_text = f.read()

    model = MODEL_MAP["coder"]

    print("\n======================")
    print(f"[TASK] {task_file}")
    print(f"[MODEL] {model}")
    print("======================\n")

    result = call_model(model, task_text)
    output = result["text"]

    out_file = task_file.replace(".md", "_result.md")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"[DONE] {out_file}")

    return out_file


def run_all_tasks(project_name):
    task_dir = tasks_path(project_name)

    if not task_dir.exists():
        print("[ERROR] no tasks")
        return

    tasks = sorted([
        f for f in os.listdir(task_dir)
        if f.startswith("TASK") and f.endswith(".md")
    ])

    for t in tasks:
        run_task_file(task_dir / t, project_name)