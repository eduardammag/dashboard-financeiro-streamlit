"""
Extração detalhada de PDFs.
"""

import pdfplumber


def load_pdf(path):
    pages = []

    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            pages.append({
                "page_number": i + 1,
                "text": text.strip(),
                "char_count": len(text)
            })

    if sum(p["char_count"] for p in pages) < 500:
        raise ValueError("PDF possivelmente escaneado (OCR futuro)")

    return {
        "type": "pdf",
        "pages": pages
    }
