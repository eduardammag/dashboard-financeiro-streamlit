"""
Detecta se o documento é predominantemente diagramático (fluxograma).
Heurística simples e robusta para MVP.
"""

import cv2
import pytesseract
from PIL import Image


def is_diagram(path: str) -> bool:
    # PDFs e imagens são candidatos
    if not path.lower().endswith((".png", ".jpg", ".jpeg", ".pdf")):
        return False

    try:
        img = Image.open(path)
        text = pytesseract.image_to_string(img)

        # Pouco texto + palavras típicas de fluxograma
        keywords = ["sim", "não", "decisão", "processo", "início", "fim"]

        keyword_hits = sum(k in text.lower() for k in keywords)

        # Fluxogramas têm pouco texto contínuo
        return len(text.strip()) < 800 or keyword_hits >= 2

    except Exception:
        return False
