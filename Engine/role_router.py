def detect_role(task: str) -> str:
    t = task.lower()

    if any(k in t for k in ["architecture", "design", "plan", "modules"]):
        return "planner"

    if any(k in t for k in ["write", "code", "function", "python", "script"]):
        return "coder"

    if any(k in t for k in ["bug", "fix", "error", "check", "review"]):
        return "qa"

    return "coder"
