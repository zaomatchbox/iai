import numpy as np


def normalize(a):
    # row_sums = a.sum(axis=1)
    # new_matrix = a / row_sums[:, np.newaxis]

    return a


def get_init_weights(p, N):
    return normalize(np.random.rand(p, N) - 1), normalize(np.random.rand(p, N) - 1)
    # return np.zeros((p, N)), np.zeros((p, N))
