import requests
import time

from Engine.role_router import detect_role
from Engine.model_map import MODEL_MAP
from Engine.storage import save_log
from Engine.task_generator import generate_tasks
from Engine.config import project_path

from Engine.contracts import CODE_GENERATION_CONTRACT
from Engine.file_writer import write_project_from_llm_output


URL = "http://localhost:11434/api/generate"


def call_model(model, prompt):
    start = time.time()

    r = requests.post(URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    if r.status_code != 200:
        raise Exception(f"Ollama error: {r.text}")

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

    # =========================
    # PROMPT BUILD
    # =========================

    if role == "coder":
        prompt = f"""
{CODE_GENERATION_CONTRACT}

TASK:
{task_text}
"""
    else:
        prompt = task_text

    # =========================
    # LLM CALL
    # =========================

    result = call_model(model, prompt)
    output = result["text"]

    # =========================
    # LOGGING
    # =========================

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

    # =========================
    # PLANNER → TASKS
    # =========================

    if role == "planner":
        tasks = generate_tasks(project_name, output)

        print("\n📦 TASKS GENERATED:")
        for t in tasks:
            print(" -", t)

    # =========================
    # CODER → FILE GENERATION
    # =========================

    if role == "coder":
        try:
            base = project_path(project_name)

            created_files = write_project_from_llm_output(
                str(base),
                output
            )

            print("\n📁 FILES CREATED:")
            for f in created_files:
                print(" -", f)

        except Exception as e:
            print("\n⚠️ FILE WRITE ERROR:")
            print(e)

    return output