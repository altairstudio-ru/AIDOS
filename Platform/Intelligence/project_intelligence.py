import os
import datetime
import json


class ProjectIntelligence:
    """
    PROJECT INTELLIGENCE LAYER

    Отвечает за превращение идеи в структуру проекта:
    - создаёт папку проекта
    - создаёт задачи (TASK-001.md и т.д.)
    - генерирует базовый план выполнения
    """

    def __init__(self, base_path="Projects"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    # ----------------------------
    # MAIN ENTRY
    # ----------------------------

    def create_project(self, idea: str):
        """
        Главная функция: идея → проект
        """

        project_name = self._normalize_name(idea)
        project_path = os.path.join(self.base_path, project_name)

        os.makedirs(project_path, exist_ok=True)
        os.makedirs(os.path.join(project_path, "Tasks"), exist_ok=True)

        plan = self._generate_plan(idea)

        # сохраняем план проекта
        with open(os.path.join(project_path, "PROJECT_PLAN.json"), "w",
encoding="utf-8") as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)

        # создаём задачи
        task_files = self._create_tasks(project_path, plan)

        return {
            "project": project_name,
            "path": project_path,
            "tasks": task_files,
            "plan": plan
        }

    # ----------------------------
    # PLAN GENERATION
    # ----------------------------

    def _generate_plan(self, idea: str):
        """
        Простейшая декомпозиция продукта
        """

        idea_low = idea.lower()

        if "suno" in idea_low or "downloader" in idea_low:
            return {
                "goal": idea,
                "modules": [
                    "requirements_analysis",
                    "architecture_design",
                    "backend_downloader",
                    "api_layer",
                    "testing",
                    "documentation"
                ],
                "agents": [
                    "Research",
                    "Executive",
                    "Backend",
                    "QA"
                ]
            }

        # fallback универсальный план
        return {
            "goal": idea,
            "modules": [
                "analysis",
                "design",
                "implementation",
                "testing"
            ],
            "agents": [
                "Research",
                "Executive",
                "Backend",
                "QA"
            ]
        }

    # ----------------------------
    # TASK CREATION
    # ----------------------------

    def _create_tasks(self, project_path: str, plan: dict):
        """
        Создаёт TASK-XXX.md файлы
        """

        tasks_path = os.path.join(project_path, "Tasks")
        created = []

        for i, module in enumerate(plan["modules"], start=1):

            task_file = f"TASK-{i:03d}.md"
            task_path = os.path.join(tasks_path, task_file)

            content = f"""# Task {i:03d}

Status
todo

Module
{module}

Goal
{plan['goal']}

Created
{datetime.datetime.now().isoformat()}
"""

            with open(task_path, "w", encoding="utf-8") as f:
                f.write(content)

            created.append(task_path)

        return created

    # ----------------------------
    # UTIL
    # ----------------------------

    def _normalize_name(self, idea: str):
        """
        Превращает идею в имя папки
        """
        return idea.lower().replace(" ", "_").replace("/", "_")
