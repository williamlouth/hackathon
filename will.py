import numpy as np
import time


M = np.random.rand(500, 7)
limit = min(len(M[0]), len(M[1]))
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

def one_entry_row(A):               # checks if there is a student with only one job left
    for row in range(len(A)):
        if count_not_nans(A[row]) == 1:
            return row

def options_left(A):
    A = A[~np.isnan(A).all(axis=1)]
    A = A[:, ~np.isnan(A).all(axis=0)]
    return A.shape


pairs = []  # the list of matches

def delete_pairs(A):    # turns student row into nans if assigned to a job
    while True:
        col = one_entry_column(A)   # checks if there is a column with one student left
        row = one_entry_row(A)
        if col is not None:    # checking if there is a column with only 1 student available
            row = np.where(A[:,col] == np.nanmax(A[:,col]))[0][0]   # finding the last available student
            #print([row, col])
            pairs.append([row, col])        # appending the match to the list
            A[row] *= np.nan    # setting student to unavailable for other jobs
        elif options_left(A)[0] <= options_left(A)[1] and row is not None:
            col = np.where(A[row] == np.nanmax(A[row]))[0][0]
            pairs.append([row, col])
            A[:,col] *= np.nan
        else:
            return A


def iterate(A):     # implementing the process
    return delete_pairs(delete_smallest(A))


def print_if(text, print_it):
    if print_it:
        #print(text)

def iter_loop(A, print_it=True):
    st = time.time()
    while True:
        A = iterate(A)
        #print(A,'\n\n')
        if len(pairs) == limit or len(A[~np.isnan(A)]) == 0:
            break
    #print(pairs)
    #print(len(pairs))
    end = time.time()
    #print(end - st)
    return pairs

iter_loop(M)


