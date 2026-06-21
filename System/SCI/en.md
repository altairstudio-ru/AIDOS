# System Command Interface (SCI)

## 1. Purpose

SCI is the single entry point for all system operations.

The user provides a natural language goal,
and the system executes full AI Development OS pipeline automatically.

---

## 2. Input

Any human instruction, for example:

- "Build SUNO downloader service"
- "Create analytics dashboard"
- "Research API for X"

No formatting required.

---

## 3. Processing Pipeline

When input is received, SCI triggers:

### Step 1 — Language Layer
Normalize input (RU/EN → internal EN structure)

---

### Step 2 — Bootstrap Engine
Initialize system execution state

---

### Step 3 — Task Generator
Break goal into structured tasks

---

### Step 4 — Router
Assign roles and create task files

---

### Step 5 — Execution Loop
Start task execution lifecycle

---

## 4. Output Behavior

SCI does NOT return raw execution details.

It provides:

- status updates
- final results
- key milestones

---

## 5. System Rule

SCI is the ONLY entry point to the system.

All other layers are internal.

---

## 6. Internal Transparency

All actions are persisted in:

- Tasks/
- Knowledge/
- Decisions/
- Registry/
- Logs/

---

## 7. Final Principle

SCI transforms human intent into a fully executed system workflow.
