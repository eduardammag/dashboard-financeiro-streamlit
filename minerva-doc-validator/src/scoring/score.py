def final_score(f):
    score = 0

    score += max(0, 1 - f["avg_paragraph_length"] / 300) * 25
    score += f["semantic_coherence"] * 25
    score += min(f["rag_retrieval_score"], 1.0) * 40
    score += min(f["num_sections"] / 10, 1) * 10

    return round(score, 2)
