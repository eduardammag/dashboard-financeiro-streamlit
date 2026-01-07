from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_features(doc):
    paragraphs = [p for s in doc for p in s["paragraphs"]]

    if len(paragraphs) < 2:
        return {"semantic_coherence": 1.0}

    emb = model.encode(paragraphs, normalize_embeddings=True)
    sims = [float(np.dot(emb[i], emb[i+1])) for i in range(len(emb)-1)]

    return {"semantic_coherence": sum(sims) / len(sims)}
