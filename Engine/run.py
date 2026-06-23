import sys
from Platform.Intelligence.project_intelligence import ProjectIntelligence
from Platform.Runtime.ExecutionEngine import ExecutionEngine


def run_idea(idea: str):
    print("[AIDOS] START IDEA:", idea)

    pi = ProjectIntelligence()

    print("[AIDOS] Creating project...")

    project = pi.create_project(idea)

    print("[AIDOS] PROJECT CREATED:", project)

    engine = ExecutionEngine()

    print("[AIDOS] EXECUTING TASKS...")

    for task_path in project.get("tasks", []):
        print("[AIDOS] TASK:", task_path)
        engine.execute_task(task_path)

    print("[AIDOS] DONE")


if __name__ == "__main__":
    print("[AIDOS] BOOT")

    if len(sys.argv) < 2:
        print("[ERROR] No idea provided")
        sys.exit(1)

    idea = sys.argv[1]
    run_idea(idea)
