import numpy as np


def normalize(distribution, grade):
    return np.sum(distribution[5 - grade:]) / np.sum(distribution)


# Investment Banking is for losers