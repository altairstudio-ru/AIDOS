# Agent Protocol (Execution Core)

## 1. Purpose

This protocol defines how any execution unit (AI model, tool, or human) operates inside the AI Development OS.

All execution must follow this protocol without exception.

---

## 2. Execution Model

Every task follows the same lifecycle:

1. Receive task
2. Load required context from files
3. Execute task
4. Write results back to files
5. Update related knowledge (if applicable)
6. Report completion
7. Terminate execution

No persistent memory is allowed between tasks.

---

## 3. Context Rules

Before execution, the worker MUST read:

- Task file
- Related project files
- Relevant knowledge base entries
- Applicable system rules

No external assumptions are allowed.

---

## 4. Output Rules

All results MUST be written to files.

Allowed outputs:
- Project updates
- Knowledge updates
- Task status updates
- Decision records
- Reports

Chat-style responses are NOT valid system output.

---

## 5. Role Separation

Execution is performed by roles, not models.

Roles define responsibility:
- Backend
- Frontend
- Research
- QA
- Knowledge
- DevOps
- Reviewer

Models are interchangeable executors of roles.

---

## 6. Ephemeral Execution Principle

Each execution unit:

- is created for a single task
- does not retain memory
- terminates after completion

---

## 7. State Authority

The only source of truth is the file system.

If conflict exists between:
- memory
- conversation
- model output

→ files ALWAYS override.

---

## 8. Knowledge Update Rule

If new validated information is discovered:

- it MUST be written to Knowledge/
- it MUST be structured
- it MUST be reusable across projects

---

## 9. Decision Logging

All non-trivial decisions MUST be recorded in:

Decisions/

Each decision must include:
- context
- reasoning
- consequences

---

## 10. Failure Handling

If execution fails:

1. Record failure in Logs/
2. Describe cause
3. Suggest correction
4. Terminate task

No silent failures are allowed.

---

## 11. Completion Definition

A task is considered complete only when:

- output is written to files
- state is updated
- no unresolved steps remain
- dependencies are documented

---

## 12. Final Rule

The system does not “respond”.

The system **executes and persists state**.
