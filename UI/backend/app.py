from fastapi import FastAPI
from pydantic import BaseModel

import sys
import os

# подключаем Engine
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(os.path.join(BASE_DIR, "Engine"))

from run import run_sci_api


app = FastAPI(title="AI Development OS Control Panel")


# =========================
# INPUT MODEL
# =========================

class TaskRequest(BaseModel):
    text: str


# =========================
# SCI ENDPOINT
# =========================

@app.post("/sci")
def sci_endpoint(req: TaskRequest):
    result = run_sci_api(req.text)
    return result


# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def root():
    return {
        "status": "AI-Development-OS UI is running"
    }
