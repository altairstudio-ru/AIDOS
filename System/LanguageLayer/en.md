# Language Layer (Semantic Bridge)

## 1. Purpose

Enables the system to accept input in natural human language (e.g. Russian)
and internally operate in a normalized English system format.

---

## 2. Core Principle

User speaks in ANY language.

System converts all intent into:

→ structured English internal representation

---

## 3. Input Handling

All incoming goals:

- Russian
- English
- mixed language
- informal speech

are valid.

---

## 4. Normalization Process

### Step 1 — Intent Extraction
Extract:
- goal
- constraints
- domain
- implicit requirements

---

### Step 2 — Translation to System Language
Convert to:

- canonical English task format
- system-compatible structure

---

### Step 3 — Forward to Bootstrap Engine
Normalized input is passed to:

→ Bootstrap Engine

---

## 5. Output Behavior

System may:
- keep internal EN structure
- optionally mirror RU explanations for user

---

## 6. Registry Rule

Both versions can exist:

- raw user intent (RU)
- system intent (EN)

They must be linked in Registry.

---

## 7. Final Principle

The system is language-agnostic at input,
but structurally consistent internally.
