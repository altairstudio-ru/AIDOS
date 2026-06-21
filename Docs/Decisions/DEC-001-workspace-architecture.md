# DEC-001 — Workspace Architecture

---

# Status
Accepted

---

# Decision

System uses Workspaces instead of Projects as primary unit of work.

---

# Context

Originally system was based on "Projects/" structure.

This created:
- mixing of responsibilities
- weak isolation between tasks
- difficulty scaling to multiple agents

---

# Alternatives considered

## 1. Keep Projects
- simpler
- but not scalable

## 2. Hybrid Projects + Workspaces
- too complex
- unclear boundaries

## 3. Workspace model (selected)
- full isolation
- scalable
- agent-friendly
- supports multi-project execution

---

# Consequences

## Positive
- clear separation of projects
- independent execution environments
- better scalability
- easier agent routing

## Negative
- more initial structure complexity
- requires workspace management layer

---

# Related systems

- WorkspaceLoader
- SCI
- Task Generator

---

# Notes

This decision is foundational for entire system architecture.
