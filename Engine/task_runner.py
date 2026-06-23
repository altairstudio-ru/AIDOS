import os
from Engine.executor import call_model
from Engine.model_map import MODEL_MAP


def read_task(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_title(task_text):
    for line in task_text.split("\n"):
        if "Title" in line:
            return line.replace("Title", "").strip()
    return "unknown"


def detect_agent(task_text):
    for line in task_text.split("\n"):
        if "Agent" in line:
            if "qa" in line.lower():
                return "qa"
            if "planner" in line.lower():
                return "planner"
    return "coder"


def run_task_file(task_file, project_path):
    task_text = read_task(task_file)

    agent = detect_agent(task_text)
    model = MODEL_MAP.get(agent, "qwen2.5-coder:7b")

    print("\n======================")
    print(f"[TASK] {task_file}")
    print(f"[AGENT] {agent}")
    print(f"[MODEL] {model}")
    print("======================\n")

    result = call_model(model, task_text)

    output = result["text"]

    # сохраняем результат рядом с задачей
    out_path = task_file.replace(".md", "_result.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"[DONE] {out_path}\n")

    return out_path


def run_all_tasks(project_path):
    tasks_dir = f"{project_path}/Tasks"

    if not os.path.exists(tasks_dir):
        print("[ERROR] No tasks found")
        return

    tasks = sorted([
        f for f in os.listdir(tasks_dir)
        if f.startswith("TASK") and f.endswith(".md")
    ])

    for t in tasks:
        task_file = os.path.join(tasks_dir, t)
        run_task_file(task_file, project_path)
