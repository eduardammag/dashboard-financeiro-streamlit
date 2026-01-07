def generate_queries(doc):
    queries = []

    for s in doc:
        if s["title"]:
            queries.append(f"O que é {s['title']}?")
        for p in s["paragraphs"][:1]:
            queries.append(f"Explique: {p[:60]}")

    return queries[:10]
