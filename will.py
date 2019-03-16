import numpy as np
import time

M = np.random.rand(1200, 20)
#print(M)

def delete_smallest(A):             # deletes the smallest entry in the matrix
    if len(A[~np.isnan(A)]) > 0:    # assuming that the matrix has at least non-nan entry
        i, j = np.where(A == np.nanmin(A))
        A[i[0]][j[0]] = np.nan
        return A


def count_not_nans(arr):            # counts the number of non-nans in an array
    return len(arr[~np.isnan(arr)])


def one_entry_column(A):            # checks if there is a column with one student left
    for col in range(len(A[0])):       # iterating through each columns
        if count_not_nans(A[:,col]) == 1:
            return col

pairs = []  # the list of matches

def delete_pairs(A):    # turns student row into nans if assigned to a job
    while True:
        col = one_entry_column(A)   # checks if there is a column with one student left
        if col is not None:    # checking if there is a column with only 1 student available
            row = np.where(A[:,col] == np.nanmax(A[:,col]))[0][0]   # finding the last available student
            print([row, col])
            pairs.append([row, col])        # appending the match to the list
            A[row] *= np.nan    # setting student to unavailable for other jobs
        else:
            return A

def iterate(A):     # implementing the process
    return delete_pairs(delete_smallest(A))

st = time.time()
while True:
    M = iterate(M)
    #print(M,'\n\n')
    if len(pairs) == 17:
        break
print(pairs)
end = time.time()
print(end - st)


