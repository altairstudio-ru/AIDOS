from Platform.Agents.base_agent import BaseAgent


class ExecutiveAgent(BaseAgent):
    """
    Executive Agent (оркестратор уровня задач):

    НЕ выполняет задачи напрямую.
    Он:
    - разбивает задачу на шаги
    - определяет порядок выполнения
    - может назначать роли другим агентам
    """

    def __init__(self):
        super().__init__("Executive")

    def execute(self, task: dict, context=None):
        """
        Планирование выполнения задачи.
        """

        content = task.get("content", "")
        knowledge = task.get("knowledge", [])
        task_type = task.get("type", "design")

        text = content.lower()

        plan = {
            "agent": self.name,
            "task_type": task_type,
            "summary": "Execution plan generated",
            "steps": [],
            "recommended_agents": [],
            "knowledge": knowledge
        }

        # ----------------------------
        # РАЗБОР ЗАДАЧИ НА ЭТАПЫ
        # ----------------------------

        if "suno" in text or "downloader" in text:
            plan["steps"].append("Analyze requirements")
            plan["steps"].append("Design architecture")
            plan["steps"].append("Implement core logic")
            plan["steps"].append("Add UI/API layer")
            plan["steps"].append("Test system")

            plan["recommended_agents"] = [
                "Research",
                "Backend",
                "Frontend",
                "QA"
            ]

        elif "api" in text:
            plan["steps"].append("Define API schema")
            plan["steps"].append("Implement endpoints")
            plan["steps"].append("Add validation")
            plan["steps"].append("Test endpoints")

            plan["recommended_agents"] = [
                "Backend",
                "QA"
            ]

        elif "ui" in text:
            plan["steps"].append("Design UI structure")
            plan["steps"].append("Build components")
            plan["steps"].append("Integrate API")
            plan["steps"].append("Test UI")

            plan["recommended_agents"] = [
                "Frontend",
                "QA"
            ]

        else:
            plan["steps"].append("Analyze task")
            plan["steps"].append("Select approach")
            plan["steps"].append("Execute implementation")
            plan["steps"].append("Validate result")

            plan["recommended_agents"] = [
                "Research",
                "QA"
            ]

        # ----------------------------
        # ИТОГ
        # ----------------------------

        return plan
