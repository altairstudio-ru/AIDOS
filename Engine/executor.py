import requests
import time

from Engine.role_router import detect_role
from Engine.model_map import MODEL_MAP
from Engine.storage import save_log
from Engine.task_generator import generate_tasks
from Engine.config import project_path


URL = "http://localhost:11434/api/generate"


def call_model(model, prompt):
    start = time.time()

    r = requests.post(URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    if r.status_code != 200:
        raise Exception(r.text)

    data = r.json()

    return {
        "text": data.get("response", ""),
        "time": round(time.time() - start, 3)
    }


def run_task(task_text: str, project_name="suno_downloader"):
    role = detect_role(task_text)
    model = MODEL_MAP[role]

    print("\n[AIDOS] BOOT")
    print(f"[AIDOS] ROLE: {role}")
    print(f"[AIDOS] MODEL: {model}")

    result = call_model(model, task_text)
    output = result["text"]

    log_path = save_log(
        project_name,
        role,
        model,
        task_text,
        output
    )

    print("\n=== OUTPUT ===\n")
    print(output)
    print(f"\n📦 LOG: {log_path}")

    # если planner → генерим задачи
    if role == "planner":
        tasks = generate_tasks(project_name, output)

        print("\n📦 TASKS GENERATED:")
        for t in tasks:
            print(" -", t)

    return output