from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def rag_score(doc, queries):
    chunks = [p for s in doc for p in s["paragraphs"]]

    if not chunks or not queries:
        return 0.0

    chunk_emb = model.encode(chunks, normalize_embeddings=True)
    scores = []

    for q in queries:
        q_emb = model.encode([q], normalize_embeddings=True)[0]
        sims = [float(np.dot(q_emb, c)) for c in chunk_emb]
        scores.append(max(sims))

    return sum(scores) / len(scores)
