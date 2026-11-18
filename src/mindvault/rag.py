from mindvault.components import ask_llm, retrieve
from mindvault.components.chunker import chunk_text
from mindvault.components.loader import load_file
from mindvault.components.retriever import build_index


chunks = chunk_text(load_file(), chunk_size=5, overlap=2)
doc_vecs = build_index(chunks)


while True:
    question = input("Ask: ").strip()
    if not question:
        continue

    context = "\n\n".join(retrieve(question, chunks, doc_vecs))
    prompt = (
        "Answer the question using ONLY the context below.\n"
        'If the answer isn\'t in the context, say "I don\'t know".\n\n'
        f"Context:\n{context}\n\n"
        f"Question: {question}"
    )

    print("\nAnswer:")
    print(ask_llm(prompt), "\n")
