def route_task(task_text: str):
    """
    Router Intelligence v1

    Определяет:
    - какой агент нужен
    - тип задачи
    - какой контекст знаний использовать
    """

    text = task_text.lower()

    # ----------------------------
    # DEFAULT VALUES
    # ----------------------------
    agent = "Research"
    task_type = "research"
    knowledge = []

    # ----------------------------
    # DETECT BACKEND TASKS
    # ----------------------------
    if any(word in text for word in ["api", "backend", "server", "database",
"sql"]):
        agent = "Backend"
        task_type = "build"
        knowledge = ["backend", "api", "architecture"]

    # ----------------------------
    # FRONTEND TASKS
    # ----------------------------
    elif any(word in text for word in ["ui", "frontend", "react", "interface",
"page"]):
        agent = "Frontend"
        task_type = "build"
        knowledge = ["ui", "ux", "frontend"]

    # ----------------------------
    # QA TASKS
    # ----------------------------
    elif any(word in text for word in ["test", "qa", "bug", "check", "verify"]):
        agent = "QA"
        task_type = "test"
        knowledge = ["testing", "validation"]

    # ----------------------------
    # ARCHITECTURE / PLANNING
    # ----------------------------
    elif any(word in text for word in ["design", "architecture", "plan",
"system"]):
        agent = "Executive"
        task_type = "design"
        knowledge = ["architecture", "system design"]

    # ----------------------------
    # DEFAULT → RESEARCH
    # ----------------------------
    else:
        agent = "Research"
        task_type = "research"
        knowledge = ["general"]

    return {
        "agent": agent,
        "task_type": task_type,
        "knowledge_context": knowledge
    }
