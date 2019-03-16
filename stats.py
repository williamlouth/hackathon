import numpy as np
#dist = np.array([2440, 603, 128, 54, 17])

def normalize(distribution, grade):
    return np.sum(distribution[5 - grade:]) / np.sum(distribution)

# Investment Banking is for losers
