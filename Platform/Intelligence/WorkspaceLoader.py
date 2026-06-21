import os

WORKSPACES_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../Workspaces")
)

def list_workspaces():
    return [
        w for w in os.listdir(WORKSPACES_DIR)
        if os.path.isdir(os.path.join(WORKSPACES_DIR, w))
    ]

def resolve_workspace(text: str):
    text = text.lower()
    workspaces = list_workspaces()

    for ws in workspaces:
        if ws.lower() in text:
            return ws

    return "Auto-Workspace"
