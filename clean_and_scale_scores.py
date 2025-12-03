import numpy as np


def clean_and_scale_scores(scores, min_score, max_score):
    scoresMK1 = np.array(scores, dtype=float)
    if scoresMK1.ndim == 1:
        for i in range(len(scoresMK1)):
            if scoresMK1[i] < min_score:
                scoresMK1[i] = min_score
            if scoresMK1[i] > max_score:
                scoresMK1[i] = max_score
    if scoresMK1.ndim == 2:
        for i in range(scoresMK1.shape[0]):
            for j in range(scoresMK1.shape[1]):
                if scoresMK1[i,j] < min_score:
                    scoresMK1[i,j] = min_score
                if scoresMK1[i,j] > max_score:
                    scoresMK1[i,j] = max_score

    scaled = (scoresMK1 - min_score) / (max_score - min_score)
    return scaled.astype(float)
