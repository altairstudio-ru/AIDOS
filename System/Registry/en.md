# Registry

## 1. Purpose

Registry defines the relationship graph between all system entities:
- files
- roles
- tasks
- knowledge
- decisions

It enables the system to understand dependencies and impact of changes.

---

## 2. Core Concept

The system is not a set of files.

It is a **graph of relationships between files**.

---

## 3. Entity Types

Registry tracks the following entities:

- Projects
- Tasks
- Roles
- Knowledge entries
- Decisions
- System files

---

## 4. Relationships

Supported relationship types:

- depends_on
- affects
- implements
- references
- derived_from
- conflicts_with

---

## 5. Dependency Rule

If A depends_on B:

- changes in B require re-evaluation of A
- A cannot be considered valid if B is invalid

---

## 6. Change Impact Rule

Any modification must trigger:

1. Registry analysis
2. identification of affected entities
3. re-execution or review of dependent roles

---

## 7. Knowledge Linking

All Knowledge entries must be linked to:
- source project
- source decision (if exists)
- related concepts

---

## 8. Decision Integration

Each decision must register:

- what it affects
- what it replaces
- what it depends on

---

## 9. System Integrity Rule

The system is invalid if:
- dependencies are unknown
- relationships are missing
- file isolation breaks consistency

---

## 10. Execution Role

Registry is not passive.

It actively supports:
- Executive planning
- QA validation
- Knowledge evolution
- Impact analysis

---

## 11. Final Principle

Without Registry, the system is a folder structure.

With Registry, it becomes a **living system of dependencies and intelligence**.
