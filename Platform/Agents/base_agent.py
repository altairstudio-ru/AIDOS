class BaseAgent:
    """
    Базовый класс всех агентов системы.

    Все агенты наследуются отсюда и обязаны реализовать метод execute().
    """

    def __init__(self, name: str):
        self.name = name

    def execute(self, task: dict, context=None):
        """
        Основной метод выполнения задачи.

        task:
            {
                "path": str,
                "title": str,
                "content": str,
                "type": str,
                "knowledge": list
            }

        context:
            дополнительный контекст от системы (опционально)
        """
        raise NotImplementedError("Agent must implement execute()")
