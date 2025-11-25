import numpy as np

def moving_average(signal, window_size):
    n = len(signal)
    k = (window_size - 1) // 2
    result = np.zeros(n, dtype=float)
    for i in range(n):
        left = max(0, i - k)
        right = min(n - 1, i + k)
        result[i] = np.mean(signal[left:right + 1])

    return result

