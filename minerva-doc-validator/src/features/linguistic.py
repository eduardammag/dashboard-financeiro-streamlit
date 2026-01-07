"""
Features linguísticas robustas para PDFs.
"""

def linguistic_features(doc):
    total_words = sum(len(s.split()) for s in doc.sections)

    return {
        "avg_words_per_section": total_words / max(len(doc.sections), 1),
        "lexical_density": total_words / max(sum(len(s) for s in doc.sections), 1)
    }
