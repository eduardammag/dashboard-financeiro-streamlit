"""
Dispatcher de carregamento de documentos.
PDF é tratado como formato prioritário.
"""

from pathlib import Path
from src.ingestion.pdf_loader import load_pdf


def load_document(path: str):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(path)

    if path.suffix.lower() == ".pdf":
        return load_pdf(path)

    if path.suffix.lower() in {".txt", ".md"}:
        return {
            "type": "text",
            "text": path.read_text(encoding="utf-8")
        }

    raise NotImplementedError(f"Formato não suportado: {path.suffix}")
