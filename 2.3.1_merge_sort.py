import math
def merge(A, p, q, r):
    L, R = A[p:q] + [math.inf], A[q:r] + [math.inf]
    i, j = 0, 0
    while i+j < r-p:
        if L[i] <= R[j]:
            A[p+i+j] = L[i]
            i += 1
        else :
            A[p+i+j] = R[j]
            j += 1

def merge_sort(A, *args):
    if args:
        p, r = args 
    else:
        merge_sort(A, 0, len(A))
        return
    if r-p <= 1: return 
    q = (p + r + 1) // 2 
    merge_sort(A, p, q)
    merge_sort(A, q, r)
    merge(A, p, q, r)


if __name__ == "__main__":
    import random
    A = list(range(1, 21))
    random.shuffle(A)
    print(A)
    merge_sort(A)
    print(A)