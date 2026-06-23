import os
import json
import datetime
import re
from Platform.Intelligence.llm import LLM


class ProjectIntelligence:
    """
    v0.7 stable — LLM-based project generator
    """

    def __init__(self, base_path="Projects"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)
        self.llm = LLM()

    # ----------------------------
    # PUBLIC
    # ----------------------------

    def create_project(self, idea: str):
        project_name = self._normalize_name(idea)
        project_path = os.path.join(self.base_path, project_name)

        os.makedirs(project_path, exist_ok=True)
        os.makedirs(os.path.join(project_path, "Tasks"), exist_ok=True)

        plan = self._generate_llm_plan(idea)

        print("[DEBUG PLAN]", plan)

        plan_path = os.path.join(project_path, "PROJECT_PLAN.json")
        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)

        tasks = self._create_tasks(project_path, plan)

        return {
            "project": project_name,
            "path": project_path,
            "plan": plan,
            "tasks": tasks
        }

    # ----------------------------
    # LLM CORE
    # ----------------------------

    def _generate_llm_plan(self, idea: str):
        prompt = f"""
You are AIDOS Project Architect.

Convert idea into structured JSON.

Return ONLY JSON:

{{
  "goal": "string",
  "modules": [
    {{
      "name": "string",
      "description": "string",
      "owner_agent": "Backend | Frontend | QA | Research | Executive"
    }}
  ],
  "execution_strategy": "sequential"
}}

Idea:
{idea}
"""

        raw = self.llm.generate(prompt)

        print("[DEBUG LLM RAW]\n", raw)

        return self._safe_parse_json(raw)

    # ----------------------------
    # TASK GENERATION
    # ----------------------------

    def _create_tasks(self, project_path: str, plan: dict):
        tasks_dir = os.path.join(project_path, "Tasks")

        modules = plan.get("modules", [])
        created = []

        for i, module in enumerate(modules, start=1):
            task_file = f"TASK-{i:03d}.md"
            task_path = os.path.join(tasks_dir, task_file)

            content = f"""# Task {i:03d}

Name: {module.get('name')}
Description: {module.get('description')}
Owner: {module.get('owner_agent')}

Created: {datetime.datetime.now().isoformat()}
"""

            with open(task_path, "w", encoding="utf-8") as f:
                f.write(content)

            created.append(task_path)

        return created

    # ----------------------------
    # UTIL
    # ----------------------------

    def _normalize_name(self, idea: str):
        return idea.lower().replace(" ", "_").replace("/", "_")

    def _safe_parse_json(self, text: str):
        text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)
        except:
            pass

        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except:
                pass

        raise ValueError(f"Invalid LLM JSON:\n{text}")
