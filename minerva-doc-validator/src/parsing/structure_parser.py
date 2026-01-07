"""
Parser estrutural.
PDF recebe tratamento detalhado.
"""

from src.parsing.pdf_document import PDFDocument
from src.parsing.text_document import TextDocument
from src.ingestion.cleaner import clean_text


def parse_structure(doc):
    if doc["type"] == "pdf":
        sections = []
        for page in doc["pages"]:
            cleaned = clean_text(page["text"])
            if len(cleaned) > 200:
                sections.append(cleaned)
        return PDFDocument(sections=sections, pages=doc["pages"])

    # texto simples
    text = clean_text(doc["text"])
    sections = [s for s in text.split("\n\n") if len(s) > 100]
    return TextDocument(sections)
