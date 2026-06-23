import requests


class LLM:
    def __init__(self, model="t-tech/T-lite-it-2.1:q6_K"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        response = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })

        # защита от HTTP ошибок
        response.raise_for_status()

        data = response.json()

        # нормальный ответ Ollama
        if "response" in data:
            return data["response"]

        # альтернативные форматы
        if "message" in data:
            return data["message"]

        if "error" in data:
            raise RuntimeError(f"Ollama error: {data['error']}")

        raise RuntimeError(f"Unknown LLM response format: {data}")
