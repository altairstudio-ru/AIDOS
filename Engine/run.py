import sys
from Engine.init import init_project


if __name__ == "__main__":
    idea = " ".join(sys.argv[1:])

    if not idea:
        print("Usage: python3 Engine/run.py \"idea\"")
        exit(1)

    init_project(idea)