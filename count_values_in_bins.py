import numpy as np

def count_values_in_bins(data, bin_edges):
    B = len(bin_edges) - 1
    counts = np.zeros(B, dtype=int)

    if data.size == 0:
        return counts
    for value in data:
        if value < bin_edges[0] or value > bin_edges[-1]:
            continue
        if value == bin_edges[-1]:
            counts[-1] += 1
            continue
        idx = np.searchsorted(bin_edges, value, side='right') - 1
        if 0 <= idx < B:
            counts[idx] += 1

    return counts

