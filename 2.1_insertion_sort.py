def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

if __name__ == '__main__':
    import random
    A = list(range(1, 21))
    random.shuffle(A)
    print(A)
    A = insertion_sort(A)
    print(A)
            