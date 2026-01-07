def explain(f):
    problems = []

    if f["avg_paragraph_length"] > 300:
        problems.append("Parágrafos excessivamente longos.")

    if f["semantic_coherence"] < 0.5:
        problems.append("Baixa coerência semântica entre trechos.")

    if f["rag_retrieval_score"] < 0.4:
        problems.append("Conteúdo difícil de recuperar via busca vetorial.")

    if not problems:
        return "Documento bem formatado para uso em RAG."

    return {
        "problems": problems,
        "recommendations": [
            "Converter diagramas em texto estruturado",
            "Dividir parágrafos longos",
            "Adicionar títulos claros e hierárquicos"
        ]
    }
