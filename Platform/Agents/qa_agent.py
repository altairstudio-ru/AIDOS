from Platform.Agents.base_agent import BaseAgent


class QAAgent(BaseAgent):
    """
    Агент контроля качества (QA):
    - проверка результата других агентов
    - поиск ошибок
    - валидация логики
    """

    def __init__(self):
        super().__init__("QA")

    def execute(self, task: dict, context=None):
        """
        Проверяет результат выполнения задачи.
        """

        content = task.get("content", "")
        knowledge = task.get("knowledge", [])
        task_type = task.get("type", "test")

        response = {
            "agent": self.name,
            "task_type": task_type,
            "summary": "QA check completed",
            "issues": [],
            "warnings": [],
            "status": "ok"
        }

        text = content.lower()

        # ----------------------------
        # ПРОВЕРКА НА ЯВНЫЕ ПРОБЛЕМЫ
        # ----------------------------

        if "error" in text:
            response["issues"].append("Detected 'error' in task content")

        if "todo" in text:
            response["warnings"].append("Task still contains TODO state")

        if "fix" in text:
            response["warnings"].append("Fix-related task detected, verify
resolution")

        # ----------------------------
        # ПРОВЕРКА СТРУКТУРЫ
        # ----------------------------

        if len(content.strip()) < 50:
            response["warnings"].append("Task description is very short")

        # ----------------------------
        # КОНТЕКСТ ОТ ROUTER
        # ----------------------------

        if knowledge:
            response["warnings"].append(
                f"QA context domains: {', '.join(knowledge)}"
            )

        # ----------------------------
        # ИТОГОВЫЙ СТАТУС
        # ----------------------------

        if response["issues"]:
            response["status"] = "failed"
        elif response["warnings"]:
            response["status"] = "needs_review"
        else:
            response["status"] = "ok"

        return response
