from merge_sort import merge_sort
from insertion_in_merge import merge_sort as imerge_sort
import time
import random

a, b, c = [], [], []

for i in range(100):
    l = [random.randint(1, 1000) for _ in range(10000)]
    A = l[:]
    t1 = time.time()
    merge_sort(A)
    t2 = time.time()
    a.append(t2-t1)
    A = l[:]
    t1 = time.time()
    imerge_sort(A)
    t2 = time.time()
    b.append(t2-t1)
    t1= time.time()
    l.sort()
    t2 = time.time()
    c.append(t2-t1)
import statistics
print(statistics.median(a), statistics.median(b), statistics.median(c))
