from datetime import datetime
from Engine.config import logs_path


def save_log(project_name, role, model, input_text, output_text):
    log_dir = logs_path(project_name)
    log_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = log_dir / f"{role}_{model}_{ts}.md"

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

    path.write_text(content, encoding="utf-8")
    return str(path)