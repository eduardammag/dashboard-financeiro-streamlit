"""
Representação estruturada de um PDF.
"""

class PDFDocument:
    def __init__(self, sections, pages):
        self.sections = sections
        self.pages = pages
