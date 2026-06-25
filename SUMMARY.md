```md
# SUMMARY.md — AIDOS (AI Development Operating System)

## 📌 Общая идея проекта

AIDOS — это автономная система разработки программного обеспечения, которая использует LLM-модели (через Ollama) для генерации, планирования и исполнения кода в 
виде агентной архитектуры.

Система работает как “OS для разработки”, где:
- пользователь задаёт задачу текстом
- система сама планирует структуру
- распределяет роли агентов
- генерирует файлы проекта
- логирует результат выполнения

---

## 🧠 Архитектура системы

### Основной pipeline

````

User Prompt
↓
Engine/run.py
↓
Engine/init.py (инициализация проекта)
↓
Engine/executor.py (LLM вызовы)
↓
Model (Ollama)
↓
JSON output (структура файлов)
↓
File Writer (создание проекта)

``

---

## ⚙️ Основные компоненты

### 📁 Engine/run.py
Точка входа.

Функции:
- принимает user prompt
- запускает init_project
- запускает полный цикл генерации

---

### 📁 Engine/init.py
Инициализация проекта.

Функции:
- создание структуры проекта
- запуск первого planner/coder этапа
- подготовка задач для executor

---

### 📁 Engine/executor.py
Ядро системы LLM execution.

Функции:
- формирует prompt для модели
- отправляет запрос в Ollama
- получает ответ
- извлекает JSON
- возвращает структурированные файлы

Ключевая ответственность:
👉 превращение LLM output → структурированные файлы

---

### 📁 Engine/models.py
Абстракция моделей.

Функции:
- маппинг имени модели
- подготовка к будущему multi-model routing

---

## 🤖 Используемые модели (Ollama)

Текущий стек:

- qwen3.5:9b → planner / architecture
- qwen2.5-coder:7b → coder (быстрый)
- qwen2.5-coder:14b → coder (качество)
- mistral:7b → универсальная модель
- starcoder2:7b → кодовая модель

---

## 🧩 Роли системы

### 📐 Planner
- создаёт архитектуру проекта
- разбивает задачу на модули
- определяет структуру файлов

---

### 💻 Coder
- генерирует код файлов
- реализует модули
- пишет функции и классы

---

### 🧪 QA (планируется)
- проверка корректности кода
- поиск ошибок
- оценка качества генерации

---

## 📦 Формат обмена (critical)

Система ожидает от LLM:

```json
{
  "project": {
    "entrypoint": "main.py",
    "modules": [
      {
        "path": "file.py",
        "content": "code"
      }
    ]
  }
}
````

---

## ⚠️ Известные проблемы системы

### ❌ JSON instability

* LLM иногда возвращает невалидный JSON
* multiline strings могут ломать парсинг

---

### ❌ API mismatch Ollama

* `/api/generate` vs `/api/chat`
* требуется единый адаптер

---

### ❌ executor fragility

* парсинг ответа LLM чувствителен к формату
* нет строгой схемы валидации

---

### ❌ отсутствует schema enforcement

* нет гарантии структуры ответа
* нет JSON schema validator

---

## 📂 Текущая структура проекта

```
AIDOS/
├── Engine/
│   ├── run.py
│   ├── init.py
│   ├── executor.py
│   └── models.py
│
├── Projects/
│   └── <generated projects>/
│
├── Logs/
│   └── model execution logs
│
└── System/
    ├── Vision/
    └── Prompts/
```

---

## 🚀 Текущий статус системы

### Что работает:

* запуск LLM через Ollama
* генерация архитектуры проекта
* генерация файлов
* запись результатов

---

### Что нестабильно:

* JSON output parsing
* API compatibility (generate/chat)
* отсутствие строгого контракта LLM

---

## 🧭 Следующие этапы развития

### 1. Stable Execution Layer

* единый LLM adapter
* schema validation
* fallback parsing

---

### 2. Multi-Agent system upgrade

* planner / coder / qa separation стабильно
* role-based prompt routing

---

### 3. File system writer v2

* атомарная запись файлов
* защита от повреждённых outputs

---

### 4. Project intelligence layer

* анализ результатов генерации
* авто-рефакторинг проектов

---

## 🧠 Ключевая идея AIDOS

AIDOS — это не генератор кода.

Это:

> система управления агентами разработки, где LLM — это исполнители ролей, а не просто чат-модель

---

## 📌 Итог

Проект сейчас находится в стадии:

> “working prototype with unstable execution layer”

Следующий шаг — стабилизация контракта между LLM и engine.

```
```
