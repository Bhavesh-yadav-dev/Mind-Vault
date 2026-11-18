import requests
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA = os.getenv("OLLAMA")
CHAT_MODEL = os.getenv("CHAT_MODEL")


def ask_llm(prompt: str) -> str:
    r = requests.post(
        f"{OLLAMA}/api/chat",
        json={
            "model": CHAT_MODEL,
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    r.raise_for_status()
    return r.json()["message"]["content"]
