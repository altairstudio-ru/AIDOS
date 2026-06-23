import os
import json
from collections import defaultdict, deque
from Platform.Runtime.ExecutionEngine import ExecutionEngine


class DAGExecutionEngine:
    """
    v0.8 — графовый исполнитель задач

    Добавляет:
    - зависимости задач
    - параллельные ветки (логически)
    - топологическую сортировку
    """

    def __init__(self):
        self.executor = ExecutionEngine()

    # ----------------------------
    # MAIN ENTRY
    # ----------------------------

    def execute_project(self, project_path: str):
        """
        Запуск всего проекта как графа задач
        """

        tasks = self._load_tasks(project_path)
        graph = self._build_graph(tasks)

        order = self._topological_sort(graph)

        results = {}

        for level in order:
            batch_results = []

            for task_path in level:
                result = self.executor.execute_task(task_path)
                batch_results.append(result)

            results[str(level)] = batch_results

        return results

    # ----------------------------
    # LOAD TASKS
    # ----------------------------

    def _load_tasks(self, project_path: str):
        tasks_dir = os.path.join(project_path, "Tasks")
        return [
            os.path.join(tasks_dir, f)
            for f in os.listdir(tasks_dir)
            if f.endswith(".md")
        ]

    # ----------------------------
    # BUILD GRAPH
    # ----------------------------

    def _build_graph(self, tasks):
        """
        Пока упрощённый DAG:
        зависимости читаются из файла (если есть DEPENDS)
        """

        graph = defaultdict(list)
        indegree = defaultdict(int)

        task_map = {}

        for t in tasks:
            task_map[t] = self._read_task(t)

        for task_path, task in task_map.items():
            depends = self._extract_dependencies(task)

            for dep in depends:
                graph[dep].append(task_path)
                indegree[task_path] += 1

            if task_path not in indegree:
                indegree[task_path] = indegree.get(task_path, 0)

        return {"graph": graph, "indegree": indegree}

    # ----------------------------
    # TOPO SORT
    # ----------------------------

    def _topological_sort(self, graph_data):
        graph = graph_data["graph"]
        indegree = graph_data["indegree"]

        queue = deque([n for n in indegree if indegree[n] == 0])

        levels = []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node)

                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue.append(neigh)

            levels.append(level)

        return levels

    # ----------------------------
    # TASK PARSER
    # ----------------------------

    def _read_task(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def _extract_dependencies(self, task_text):
        """
        Ищем DEPENDS: TASK-001.md
        """

        deps = []

        for line in task_text.splitlines():
            if line.startswith("DEPENDS:"):
                dep = line.replace("DEPENDS:", "").strip()
                deps.append(dep)

        return deps
