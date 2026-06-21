# Task Router

## 1. Purpose

The Router is responsible for:
- receiving tasks or goals
- converting them into structured tasks
- assigning roles
- triggering execution flow

It is the bridge between intent and execution.

---

## 2. Input Types

The system accepts:

- User goals
- Executive plans
- Subtasks
- System triggers

---

## 3. Output

The Router produces:

- Task files in /Tasks/
- Role assignments
- Execution queue updates

---

## 4. Routing Logic

### Step 1 — Interpret Intent
Determine:
- what is requested
- scope of work
- complexity

---

### Step 2 — Decompose
Split into atomic tasks:
- research
- backend
- frontend
- QA

---

### Step 3 — Assign Role
Map each task to a role:
- Research → analysis tasks
- Backend → implementation
- QA → validation

---

### Step 4 — Create Task Files
Each task MUST be written as a file:

/Tasks/TASK-XXX.md

---

### Step 5 — Register in Execution Loop
Tasks are added to execution queue.

---

## 5. Constraints

- Router does NOT execute work
- Router does NOT produce final results
- Router only structures and assigns

---

## 6. Dependency Awareness

Router MUST consult Registry before:
- assigning tasks
- splitting work
- parallel execution decisions

---

## 7. Final Principle

Router converts chaos (intent) into structure (tasks).
