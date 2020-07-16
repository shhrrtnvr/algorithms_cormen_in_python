import math
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

def insertion_sort(A, p, r):
    for i in range(p+1,r):
        key = A[i]
        j = i-1
        while j >= p and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def merge_sort(A, *args):
    if args:
        p, r, k = args
    else:
        merge_sort(A, 0, len(A), math.ceil(math.log2(len(A))))
        return
    q = (p+r+1)//2
    if q-p <= k:
        insertion_sort(A, p, q)
    else:
        merge_sort(A, p, q, k)
    if r-q <= k:
        insertion_sort(A, q, r)
    else:
        merge_sort(A, q, r, k)
    merge(A,p,q,r)
        
if __name__ == '__main__':
    import random
    A = list(range(1, 21))
    random.shuffle(A)
    print(A)
    merge_sort(A)
    print(A)
