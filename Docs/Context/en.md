# AI Development OS — Project Context (v1)

---

# How to use this file

If you are an AI agent:

1. Read this file first.
2. It describes the system architecture and decisions.
3. Treat it as source of truth for system design.
4. Do not override decisions unless explicitly instructed.
5. Propose improvements instead of silent changes.

---

# 1. Vision

AI Development OS is a model-agnostic development operating system.

Its goal is:

- Transform natural language tasks into structured execution
- Automatically route tasks to appropriate agents
- Maintain persistent file-based memory
- Enable multi-project development through isolated Workspaces

---

# 2. Core Idea

The system is built around:

- SCI (System Command Interface) as entry point
- Workspace-based project isolation
- Agent-based execution model
- Markdown as the main memory format

---

# 3. Key Principles

- Files are the source of truth
- No hidden state in runtime memory
- Every action is persisted in filesystem
- English is canonical language for system logic
- Russian is auxiliary for human understanding
- System must remain model-agnostic

---

# 4. System Architecture

## Layers

User Input
  ↓
SCI Layer
  ↓
Workspace Resolver
  ↓
Task Generator
  ↓
Agent Router
  ↓
Execution Layer
  ↓
File System (Source of Truth)
  ↓
Memory / Knowledge Update

---

# 5. Workspace Concept

Workspace = isolated project environment.

Each workspace contains:

- Tasks/
- Knowledge/
- Decisions/
- Logs/
- workspace.json

Example:

Workspaces/Suno-Downloader/

Workspaces are independent and self-contained.

---

# 6. Task System

Tasks are stored as Markdown files:

- TASK-001.md
- TASK-002.md

Each task contains:

- Description
- Role assignment
- Status
- Execution notes

---

# 7. SCI (System Command Interface)

SCI is the main entry point of the system.

It:

- Receives natural language input
- Normalizes it
- Sends it to Workspace Resolver
- Triggers Task creation

---

# 8. Agent System

Planned roles:

- Executive — final decision maker
- Planner — task decomposition
- Research — information gathering
- Backend — implementation
- Frontend — UI development
- QA — testing
- Reviewer — validation

Agents operate on tasks, not directly on system state.

---

# 9. File Standards

- System state must always be stored in files
- No implicit runtime memory
- All changes must be persisted
- English is canonical for system logic files
- Russian may be used for readability

---

# 10. Current Decisions

- Projects concept replaced with Workspaces
- Tasks are file-based Markdown entities
- System is designed for multi-agent execution
- Routing is handled via Workspace Resolver

---

# 11. Known Limitations (v1)

- Workspace detection is keyword-based only
- No semantic understanding yet
- No real event system implemented
- No persistent agent memory
- No UI layer integration yet

---

# 12. Next Steps

- Implement SCI execution engine
- Improve Workspace resolution (semantic matching)
- Add EventBus system
- Build Memory layer for Workspaces
- Introduce UI control panel
- Add automatic CONTEXT updates

---

