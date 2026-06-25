Сделал правильно: **два полностью согласованных документа (EN + RU)** + затем я прогнал их как систему (структура → целостность → пробелы → улучшения → 
финальная версия).

---

# 📘 ARCHITECTURE.md (ENGLISH — SYSTEM VERSION)

```md id="aidos_arch_en_v2"
# AIDOS — Architecture Document

## 1. System Overview

AIDOS (AI Development Operating System) is an agent-based software generation system where LLMs act as role-based workers inside a deterministic execution 
pipeline.

The system transforms a natural language request into:
- project architecture
- task decomposition
- source code generation
- file system output
- execution logs

---

## 2. Core Design Principle

> AIDOS is not a chatbot. It is a controlled execution system for LLM-based software generation.

Key principle:
- LLM is an unreliable worker
- Engine is deterministic controller

---

## 3. System Architecture

```

User Input
↓
Engine/run.py
↓
Engine/init.py
↓
Planner Stage
↓
Task Generator
↓
Execution Engine
↓
LLM (Ollama Models)
↓
Structured JSON Output
↓
File Writer
↓
Project on Disk
↓
Logs + Artifacts

```

---

## 4. System Layers

### 4.1 Input Layer
**Engine/run.py**

Responsibilities:
- receives user prompt
- starts project lifecycle
- triggers initialization pipeline

---

### 4.2 Initialization Layer
**Engine/init.py**

Responsibilities:
- project bootstrap
- initial planning request
- task decomposition setup

---

### 4.3 Execution Layer (Core)
**Engine/executor.py**

Responsibilities:
- builds prompts for LLM
- calls Ollama API
- receives model output
- parses JSON structure
- validates schema
- returns normalized result

Critical role:
> converts unstructured LLM output into deterministic structured data

---

### 4.4 Model Layer
**Engine/models.py**

Responsibilities:
- model registry
- routing by role
- abstraction over Ollama models

---

### 4.5 File System Layer

Responsibilities:
- create project directories
- write generated files
- ensure atomic file output

---

### 4.6 Logging Layer

Responsibilities:
- store LLM outputs
- store execution traces
- debugging and replay support

---

## 5. Role-Based System

### Planner Role
- architecture design
- task decomposition
- system structuring

### Coder Role
- code generation
- module implementation
- file-level output

### QA Role (planned)
- validation of generated code
- error detection
- quality scoring

---

## 6. Execution Pipeline

```

TASK INPUT
↓
Planner → Task Graph
↓
Task Queue
↓
Coder Agent
↓
LLM Response
↓
JSON Parser
↓
Schema Validator
↓
File Writer
↓
Disk Output

````

---

## 7. Data Contract (Critical)

All LLM responses MUST follow strict schema:

```json
{
  "project": {
    "entrypoint": "main.py",
    "modules": [
      {
        "path": "file.py",
        "content": "source code"
      }
    ]
  }
}
````

No deviation allowed.

---

## 8. Known System Issues

### 8.1 JSON Fragility

* broken multiline strings
* invalid escaping
* partial responses

### 8.2 Ollama API inconsistency

* generate vs chat endpoints mismatch

### 8.3 No schema enforcement

* no strict validator layer
* no structured fallback recovery

### 8.4 Weak executor robustness

* parsing depends on raw text assumptions

---

## 9. Design Principles

* Deterministic execution over LLM creativity
* Strict contract-based communication
* Stateless execution per run
* Role separation (planner / coder / QA)
* Fail-safe parsing required

---

## 10. Current System State

Status:

> Functional prototype with unstable execution layer

Working:

* LLM integration
* role system
* project generation
* file writing

Broken:

* JSON stability
* schema enforcement
* API consistency

---

## 11. Future Improvements

### Phase 1 — Stability Layer

* JSON schema validation
* safe parsing layer
* Ollama adapter abstraction

### Phase 2 — Multi-Agent Runtime

* task queue system
* retry logic
* role orchestration engine

### Phase 3 — Autonomous Dev OS

* self-improving loops
* feedback-based refinement
* automated refactoring cycles

---

## 12. Core Vision

AIDOS is:

> A deterministic orchestration system where LLMs are replaceable workers inside a controlled execution pipeline.

Not a model. Not a chatbot.

A system.

````
