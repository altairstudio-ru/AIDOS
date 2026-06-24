from pathlib import Path

# корень проекта (AIDOS/)
ROOT = Path(__file__).resolve().parent.parent

ENGINE = ROOT / "Engine"
PLATFORM = ROOT / "Platform"
SYSTEM = ROOT / "System"
PROJECTS = ROOT / "Projects"


def project_path(name: str) -> Path:
    return PROJECTS / name


def tasks_path(name: str) -> Path:
    return PROJECTS / name / "Tasks"


def logs_path(name: str) -> Path:
    return PROJECTS / name / "Logs"