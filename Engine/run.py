import sys
from Engine.executor import run_task
from Engine.task_runner import run_all_tasks


if __name__ == "__main__":
    task = " ".join(sys.argv[1:])

    if not task:
        print("Usage: python3 Engine/run.py \"task\"")
        exit(1)

    print("[AIDOS] BOOT")

    # 🧠 1. planner + generation
    run_task(task)

    # 🚀 2. AUTONOMOUS EXECUTION
    print("\n[AIDOS] RUNNING TASKS...\n")
    run_all_tasks("AIDOS/Projects/suno_downloader")

    print("\n[AIDOS] DONE FULL CYCLE")
