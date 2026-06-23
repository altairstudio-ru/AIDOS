import datetime

from Platform.Agents.registry import get_agent
from Platform.Intelligence.router import route_task


# ----------------------------
# СТАТУС ЗАДАЧИ
# ----------------------------

def update_task_status(task_path, status):
    """
    Обновляет статус задачи в markdown файле
    """

    with open(task_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    status_written = False

    for line in lines:
        if line.strip().lower().startswith("# status"):
            new_lines.append(line)
            new_lines.append(f"{status}\n")
            status_written = True
        else:
            new_lines.append(line)

    if not status_written:
        new_lines.insert(0, f"# Status\n{status}\n\n")

    with open(task_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


# ----------------------------
# ЛОГИ
# ----------------------------

def append_log(task_path, message):
    """
    Пишет лог прямо в файл задачи
    """

    timestamp = datetime.datetime.now().isoformat()

    with open(task_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n---\n# LOG [{timestamp}]\n{message}\n")


# ----------------------------
# EXECUTION ENGINE v2
# ----------------------------

def execute_task(task_path):
    """
    Полный pipeline:

    Task → Router → Executive → Agents → Result
    """

    # 1. старт
    update_task_status(task_path, "in_progress")
    append_log(task_path, "Task started")

    # 2. читаем задачу
    with open(task_path, "r", encoding="utf-8") as f:
        task_content = f.read()

    # 3. ROUTER
    routing = route_task(task_content)

    primary_agent = routing["agent"]
    task_type = routing["task_type"]
    knowledge = routing["knowledge_context"]

    append_log(task_path, f"Router selected: {primary_agent} ({task_type})")

    task = {
        "path": task_path,
        "title": task_path.split("/")[-1],
        "content": task_content,
        "type": task_type,
        "knowledge": knowledge
    }

    # 4. EXECUTIVE LAYER (НОВОЕ)
    executive = get_agent("Executive")
    plan = executive.execute(task, context=None)

    append_log(task_path, f"Executive plan created: {plan['steps']}")

    results = []

    # 5. EXECUTION PIPELINE ПО ШАГАМ
    for agent_name in plan["recommended_agents"]:

        agent = get_agent(agent_name)
        append_log(task_path, f"Running agent: {agent.name}")

        try:
            result = agent.execute(task, context=plan)
            results.append({
                "agent": agent.name,
                "result": result
            })

            append_log(task_path, f"{agent.name} result: {result}")

        except Exception as e:
            error_msg = f"{agent.name} failed: {str(e)}"
            append_log(task_path, error_msg)
            results.append({
                "agent": agent.name,
                "error": error_msg
            })

    # 6. финализация
    update_task_status(task_path, "done")
    append_log(task_path, "Execution completed")

    return {
        "plan": plan,
        "results": results
    }
