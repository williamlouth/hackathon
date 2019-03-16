import numpy as np

#dist = np.array([2440, 603, 128, 54, 17])

def normalize(distribution, grade):
    #print(len(distribution))
    #print(grade)
    #print(distribution[(5 - grade):])
    a =  np.sum(distribution[5 - grade:]) / np.sum(distribution)
    if a ==0:
        print(a)
        print(distribution)
        print("grade  " + str(grade))
        print(distribution[5 - grade:])
    return np.sum(distribution[5 - grade:]) / np.sum(distribution)


# Investment Banking is for losers
# Investment Banking is for losers
