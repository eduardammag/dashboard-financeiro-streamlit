"""
Pipeline principal do Minerva Document Validator.

Decide automaticamente se o documento é textual ou diagramático (fluxograma),
aplica o pipeline adequado e retorna um score de adequação para uso em RAG.
"""

# 🔹 Imports devem começar com `src.` pois o projeto usa o layout `src/`
from src.ingestion.loader import load_document
from src.ingestion.cleaner import clean_text

from src.multimodal.diagram_detector import is_diagram
from src.multimodal.flowchart_parser import parse_flowchart

from src.parsing.structure_parser import parse_structure

from src.features.structural import structural_features
from src.features.linguistic import linguistic_features
from src.features.semantic import semantic_features

from src.rag_simulation.query_generator import generate_queries
from src.rag_simulation.retriever import rag_score

from src.scoring.scorer import final_score
from src.scoring.explanations import explain


def validate_document(path: str) -> dict:
    """
    Executa a validação completa de um documento.

    Parâmetros
    ----------
    path : str
        Caminho para o documento (texto ou imagem de fluxograma).

    Retorna
    -------
    dict
        Score final, features extraídas e explicação diagnóstica.
    """

    # Detecta automaticamente o tipo do documento
    if is_diagram(path):
        print(" Fluxograma detectado")
        text_representation = parse_flowchart(path)
        doc = parse_structure(text_representation)
    else:
        print(" Documento textual detectado")
        raw_text = load_document(path)
        cleaned_text = clean_text(raw_text)
        doc = parse_structure(cleaned_text)

    # 2 Extração de features estruturais, linguísticas e semânticas
    features = {}
    features.update(structural_features(doc))
    features.update(linguistic_features(doc))
    features.update(semantic_features(doc))

    #  Simulação offline de RAG (recuperabilidade)
    queries = generate_queries(doc)
    features["rag_retrieval_score"] = rag_score(doc, queries)

    # Cálculo do score final e geração da explicação
    score = final_score(features)
    explanation = explain(features)

    return {
        "score": score,
        "features": features,
        "explanation": explanation
    }


if __name__ == "__main__":
    # Exemplo de execução manual (modo script)
    result = validate_document("data/raw/exemplo_fluxograma.png")
    print(result)


#python -m src.main
#“Por que precisou instalar o Tesseract?”
#Porque o sistema precisa processar PDFs escaneados e diagramas, e isso exige OCR. 
#O pytesseract é apenas um wrapper Python; o motor OCR real é o Tesseract.”