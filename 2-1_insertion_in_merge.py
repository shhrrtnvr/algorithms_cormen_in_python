import math
from 2.1_insertion_sort import insertion_sort
def merge(A, p, q, r):
    L, R = A[p:q] + [math.inf], A[q:r] + [math.inf]
    i, j = 0, 0
    while i+j < r-p:
        if L[i] <= R[j]:
            A[p+i+j] = L[i]
            i += 1
        else:
            A[p+i+j] = R[j]
            j += 1

def sort(A, *args):
    if args:
        p, q, k = args
    else:
        sort(A, 0, len(A), math.ceil(math.log2(len(A))))
        return
    