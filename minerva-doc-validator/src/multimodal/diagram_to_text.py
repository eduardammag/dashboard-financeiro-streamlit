"""
Transforma texto fragmentado de OCR em narrativa sequencial.
Não reconstrói setas perfeitamente, mas torna RAG-friendly.
"""

def diagram_to_text(ocr_text: str) -> str:
    lines = [l.strip() for l in ocr_text.split("\n") if l.strip()]

    narrative = ["O processo descrito no fluxograma segue as seguintes etapas:"]

    for i, line in enumerate(lines, 1):
        narrative.append(f"Etapa {i}: {line}.")

    narrative.append(
        "Observação: recomenda-se converter o fluxograma em texto estruturado "
        "para melhorar a recuperação de informações."
    )

    return "\n".join(narrative)
