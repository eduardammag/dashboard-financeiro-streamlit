"""
Limpeza específica para texto extraído de PDF.
"""

import re


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\d+\s*/\s*\d+", "", text)  # remove "1/10"
    return text.strip()
