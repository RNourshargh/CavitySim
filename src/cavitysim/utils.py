import numpy as np


def path_free_space(path_length, n0):
    abcd = np.array([[1, path_length], [0, 1]])
    opl = path_length*n0

    return abcd, opl
