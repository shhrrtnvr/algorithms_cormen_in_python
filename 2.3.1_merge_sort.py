import math
def merge(A, p, q, r):
    L, R = A[p:q+1] + [math.inf], A[q+1:r] + [math.inf]
    i, j = 0, 0
    while i+j < r-p:
        if L[i] <= R[j]:
            A[p+i+j] = L[i]
            i += 1
        else :
            A[p+i+j] = R[j]
            j += 1

def merge_srt(A, p, r):
    if p >= r: return
    q = (p + r) // 2
    merge_srt(A, p, q)
    merge_srt(A, q+1, r)
    merge(A, p, q, r)

def merge_sort(A):
    merge_srt(A, 0, len(A))

if __name__ == "__main__":
    import random
    A = list(range(1, 21))
    random.shuffle(A)
    print(A)
    merge_sort(A)
    print(A)