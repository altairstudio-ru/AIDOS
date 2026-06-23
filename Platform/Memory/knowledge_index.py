import os

KNOWLEDGE_DIR = "Docs/Knowledge"

def load_knowledge():
    knowledge = []

    if not os.path.exists(KNOWLEDGE_DIR):
        return knowledge

    for file in os.listdir(KNOWLEDGE_DIR):
        if file.endswith(".md"):
            path = os.path.join(KNOWLEDGE_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                knowledge.append(f.read())

    return knowledge


def find_relevant_knowledge(query):
    knowledge = load_knowledge()

    results = []

    for k in knowledge:
        if query.lower() in k.lower():
            results.append(k)

    return results
