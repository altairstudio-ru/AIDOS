from Platform.Agents.base_agent import BaseAgent


class FrontendAgent(BaseAgent):
    """
    Агент для frontend задач:
    - UI / UX
    - страницы
    - интерфейсы
    - компоненты
    """

    def __init__(self):
        super().__init__("Frontend")

    def execute(self, task: dict, context=None):
        """
        Выполняет frontend-задачу с учетом контекста Router.
        """

        content = task.get("content", "")
        knowledge = task.get("knowledge", [])
        task_type = task.get("type", "build")

        response = {
            "agent": self.name,
            "task_type": task_type,
            "summary": "Frontend task executed",
            "details": "",
            "ui_notes": [],
            "suggestions": []
        }

        # ----------------------------
        # АНАЛИЗ UI/UX ЗАДАЧ
        # ----------------------------

        if "ui" in content.lower():
            response["details"] += "UI-related task detected. "

        if "react" in content.lower():
            response["details"] += "React-based implementation expected. "

        if "dashboard" in content.lower():
            response["details"] += "Dashboard layout required. "

        if "mobile" in content.lower():
            response["details"] += "Mobile-first design required. "

        # ----------------------------
        # КОНТЕКСТ ОТ ROUTER
        # ----------------------------

        if knowledge:
            response["suggestions"].append(
                f"Frontend knowledge domains: {', '.join(knowledge)}"
            )

        # ----------------------------
        # UI STRUCTURE HINTS
        # ----------------------------

        response["ui_notes"].append("Prefer component-based architecture")
        response["ui_notes"].append("Keep layout modular and reusable")

        response["summary"] = "Frontend analysis completed"

        return response
