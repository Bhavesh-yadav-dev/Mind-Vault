import re


def chunk_text(text: str, chunk_size: int = 5, overlap: int = 2) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    step = max(1, chunk_size - overlap)
    chunks = []
    for i in range(0, len(sentences), step):
        chunk = " ".join(sentences[i : i + chunk_size]).strip()
        if chunk:
            chunks.append(chunk)
    return chunks
