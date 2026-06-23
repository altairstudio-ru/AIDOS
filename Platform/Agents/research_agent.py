from Platform.Agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research")

    def execute(self, task, context=None):
        return f"[Research] Analyzing information for: {task['title']}"
