from Platform.Intelligence.llm import LLM


class ExecutiveAgent:
    """
    LLM-управляемый архитектор выполнения
    """

    def __init__(self):
        self.llm = LLM()

    def execute(self, task, context=None):
        prompt = f"""
You are Executive Agent in AI system AIDOS.

You are responsible for execution strategy.

PROJECT:
{task["content"]}

CONTEXT PLAN:
{context}

Return JSON ONLY:
{{
  "steps": ["..."],
  "recommended_agents": ["Backend", "Frontend", "QA"],
  "execution_mode": "sequential | parallel",
  "risks": ["..."]
}}
"""

        raw = self.llm.generate(prompt)

        return self._safe_parse(raw)

    def _safe_parse(self, text: str):
        try:
            import json
            return json.loads(text)
        except:
            start = text.find("{")
            end = text.rfind("}")
            return json.loads(text[start:end+1])
