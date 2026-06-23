from Platform.Agents.backend_agent import BackendAgent
from Platform.Agents.research_agent import ResearchAgent
from Platform.Agents.frontend_agent import FrontendAgent
from Platform.Agents.qa_agent import QAAgent
from Platform.Agents.executive_agent import ExecutiveAgent

AGENTS = {
    "Backend": BackendAgent(),
    "Research": ResearchAgent(),
    "Frontend": FrontendAgent(),
    "QA": QAAgent(),
    "Executive": ExecutiveAgent()
}

def get_agent(name):
    return AGENTS.get(name, AGENTS["Research"])
