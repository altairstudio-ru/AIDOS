# Project Intelligence Layer

## 1. Purpose

Project Intelligence Layer is responsible for mapping incoming tasks to the correct project context.

It eliminates hardcoded project routing.

---

## 2. Core Function

Input:
- Natural language task

Output:
- Selected project OR new project creation

---

## 3. Decision Flow

### Step 1 — Semantic Analysis
Extract:
- domain
- intent
- keywords
- technical scope

---

### Step 2 — Project Matching
Compare against existing projects:

/Projects/*
- name similarity
- domain overlap
- historical tasks
- knowledge context

---

### Step 3 — Scoring

Each project receives a score:

- semantic similarity
- historical relevance
- task overlap

Highest score wins.

---

### Step 4 — New Project Creation

If no match exceeds threshold:
→ create new project folder
→ register in Project Registry

---

## 4. Output

- project_name
- confidence score
- reasoning

---

## 5. System Rule

Project selection MUST be dynamic and context-based.

No hardcoded mappings allowed.
