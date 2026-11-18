import numpy as np
from .embedding import embed


def build_index(chunks: list[str]) -> np.ndarray:
    """Embed and normalise document chunks, returning the vector matrix."""
    doc_vecs = embed([f"search_document: {c}" for c in chunks])
    doc_vecs /= np.linalg.norm(doc_vecs, axis=1, keepdims=True)
    return doc_vecs


def retrieve(question: str, chunks: list[str], doc_vecs: np.ndarray, k: int = 3) -> list[str]:
    q = embed([f"search_query: {question}"])[0]
    q /= np.linalg.norm(q)
    scores = doc_vecs @ q
    top = np.argsort(scores)[::-1][:k]
    return [chunks[i] for i in top]
