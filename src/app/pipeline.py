import numpy as np

def quality_score(frame) -> float:
    # Heurística simples: variação de Laplaciano para foco
    import cv2
    return float(cv2.Laplacian(frame, cv2.CV_64F).var())
