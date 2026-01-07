"""
Extrai texto de fluxogramas usando OCR
e delega a linearização.
"""

import pytesseract
from PIL import Image
from src.multimodal.diagram_to_text import diagram_to_text


def parse_flowchart(path: str) -> str:
    image = Image.open(path)

    # OCR bruto
    raw_text = pytesseract.image_to_string(image)

    # Converte texto fragmentado em narrativa linear
    linear_text = diagram_to_text(raw_text)

    return linear_text
