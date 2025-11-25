import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    clipped = np.clip(scores, min_score, max_score)
    scaled = (clipped - min_score) / (max_score - min_score)
    return scaled.astype(float)