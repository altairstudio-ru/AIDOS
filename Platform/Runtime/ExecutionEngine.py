from Platform.Agents.registry import get_agent


class ExecutionEngine:
    """
    ExecutionEngine v0.7

    Отвечает за выполнение задач через агентов
    с поддержкой LLM-структурированных планов.
    """

    def __init__(self):
        self.registry = get_agent

    # ----------------------------
    # MAIN ENTRY
    # ----------------------------

    def execute_task(self, task_path: str, context=None):
        """
        Выполняет одну задачу из файла
        """

        task = self._load_task(task_path)

        # 1. Router → выбирает агента
        route = self._route(task)

        agent_name = route["agent"]
        agent = self.registry(agent_name)

        # 2. Executive step (если нужен LLM план)
        execution_plan = None

        if hasattr(agent, "execute"):
            execution_plan = agent.execute(
                {
                    "task": task,
                    "context": context,
                    "route": route
                }
            )

        # 3. fallback execution
        result = self._run_agent(agent, task, execution_plan)

        # 4. save result back to task
        self._save_result(task_path, result)

        return result

    # ----------------------------
    # ROUTING
    # ----------------------------

    def _route(self, task: dict):
        """
        Простая маршрутизация задач
        """

        content = task.get("content", "").lower()

        if "frontend" in content:
            return {"agent": "Frontend"}

        if "backend" in content:
            return {"agent": "Backend"}

        if "test" in content or "qa" in content:
            return {"agent": "QA"}

        # default
        return {"agent": "Executive"}

    # ----------------------------
    # AGENT EXECUTION
    # ----------------------------

    def _run_agent(self, agent, task, execution_plan):
        """
        Запуск агента
        """

        if hasattr(agent, "run"):
            return agent.run(task, execution_plan)

        return {
            "status": "executed",
            "agent": agent.__class__.__name__,
            "task": task,
            "plan": execution_plan
        }

    # ----------------------------
    # TASK LOADING
    # ----------------------------

    def _load_task(self, path: str):
        """
        Загружает markdown задачу
        """

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        return {
            "path": path,
            "content": content
        }

    # ----------------------------
    # SAVE RESULT
    # ----------------------------

    def _save_result(self, path: str, result: dict):
        """
        Записывает результат обратно в task файл
        """

        with open(path, "a", encoding="utf-8") as f:
            f.write("\n\n--- RESULT ---\n")
            f.write(str(result))
