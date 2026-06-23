import os
from datetime import datetime


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def save_log(project_path, role, model, input_text, output_text):
    ensure_dir(f"{project_path}/Logs")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f"{project_path}/Logs/{role}_{model}_{ts}.md"

    content = f"""# AIDOS LOG

## Role: {role}
## Model: {model}
## Time: {ts}

---

## INPUT
{input_text}

---

## OUTPUT
{output_text}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path
