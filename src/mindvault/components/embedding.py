import numpy as np
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA = os.getenv("OLLAMA")
EMBED_MODEL = os.getenv("EMBED_MODEL")
CHAT_MODEL = os.getenv("CHAT_MODEL")


def embed(texts: list[str]) -> np.ndarray:
    r = requests.post(
        f"{OLLAMA}/api/embed", json={"model": EMBED_MODEL, "input": texts}
    )
    r.raise_for_status()
    
    return np.array(r.json()["embeddings"])