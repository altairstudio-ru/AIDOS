import json
import re
from pathlib import Path


def extract_json(text: str) -> str:
    """
    Убирает ```json ... ``` обёртки
    """

    # убираем markdown code block
    cleaned = re.sub(r"```json", "", text)
    cleaned = re.sub(r"```", "", cleaned)

    return cleaned.strip()


def safe_write_file(base_path: Path, file_path: str, content: str):
    target = (base_path / file_path).resolve()

    if not str(target).startswith(str(base_path.resolve())):
        raise Exception(f"Unsafe path: {file_path}")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def write_project_from_llm_output(project_path: str, llm_output: str):
    base = Path(project_path).resolve()

    cleaned = extract_json(llm_output)

    try:
        data = json.loads(cleaned)
    except Exception as e:
        raise Exception(
            f"JSON parse failed:\n{e}\n\n---CLEANED OUTPUT---\n{cleaned}"
        )

    if "files" not in data:
        raise Exception("Missing 'files' key")

    created = []

    for f in data["files"]:
        path = f.get("path")
        content = f.get("content", "")

        if not path:
            continue

        safe_write_file(base, path, content)
        created.append(str(base / path))

    return created