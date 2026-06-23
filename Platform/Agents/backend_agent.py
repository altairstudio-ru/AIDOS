from Platform.Agents.base_agent import BaseAgent


class BackendAgent(BaseAgent):
    """
    Агент для backend задач:
    - API
    - серверная логика
    - базы данных
    - архитектура сервисов
    """

    def __init__(self):
        super().__init__("Backend")

    def execute(self, task: dict, context=None):
        """
        Выполняет backend-задачу с учетом контекста от Router.
        """

        content = task.get("content", "")
        knowledge = task.get("knowledge", [])
        task_type = task.get("type", "build")

        # ----------------------------
        # БАЗОВАЯ ЛОГИКА АНАЛИЗА
        # ----------------------------

        response = {
            "agent": self.name,
            "task_type": task_type,
            "summary": "Backend task executed",
            "details": "",
            "suggestions": []
        }

        # ----------------------------
        # АНАЛИЗ СОДЕРЖИМОГО
        # ----------------------------

        if "api" in content.lower():
            response["details"] += "Detected API-related task. "

        if "database" in content.lower() or "sql" in content.lower():
            response["details"] += "Database layer required. "

        if "auth" in content.lower():
            response["details"] += "Authentication system needed. "

        # ----------------------------
        # ИСПОЛЬЗОВАНИЕ КОНТЕКСТА РОУТЕРА
        # ----------------------------

        if knowledge:
            response["suggestions"].append(
                f"Use knowledge domains: {', '.join(knowledge)}"
            )

        # ----------------------------
        # РЕЗУЛЬТАТ
        # ----------------------------

        response["summary"] = "Backend analysis completed"

        return response
