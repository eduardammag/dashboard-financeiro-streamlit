"""
Features estruturais com foco em PDF.
"""

def structural_features(doc):
    feats = {
        "num_sections": len(doc.sections),
        "avg_section_length": sum(len(s) for s in doc.sections) / max(len(doc.sections), 1),
    }

    if hasattr(doc, "pages"):
        feats["num_pages"] = len(doc.pages)
        feats["avg_chars_per_page"] = sum(p["char_count"] for p in doc.pages) / len(doc.pages)

    return feats
