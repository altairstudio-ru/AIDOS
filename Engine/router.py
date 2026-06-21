def route(task_text: str) -> str:
    """
    Определяет роль по ключевым словам (MVP версия)
    """

    text = task_text.lower()

    if "api" in text or "backend" in text:
        return "Backend"

    if "ui" in text or "frontend" in text:
        return "Frontend"

    if "test" in text or "qa" in text:
        return "QA"

    return "Research"
