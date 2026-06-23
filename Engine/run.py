import sys

from Platform.Intelligence.project_intelligence import ProjectIntelligence
from Platform.Runtime.ExecutionEngine import execute_task


def run_idea(idea: str):
    """
    Главная точка входа:

    IDEA → PROJECT → TASKS → EXECUTION
    """

    print(f"[AIDOS] Starting project creation: {idea}")

    # 1. создаём проект
    pi = ProjectIntelligence()
    project = pi.create_project(idea)

    print(f"[AIDOS] Project created: {project['project']}")
    print(f"[AIDOS] Tasks generated: {len(project['tasks'])}")

    results = []

    # 2. автоматически запускаем все задачи
    for task_path in project["tasks"]:
        print(f"[AIDOS] Executing task: {task_path}")

        result = execute_task(task_path)
        results.append({
            "task": task_path,
            "result": result
        })

    print("[AIDOS] All tasks completed")

    return {
        "project": project,
        "results": results
    }


# ----------------------------
# CLI ENTRY
# ----------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run.py 'Your idea here'")
        sys.exit(1)

    idea = sys.argv[1]
    run_idea(idea)
