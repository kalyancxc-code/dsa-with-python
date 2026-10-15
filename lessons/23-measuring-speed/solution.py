"""Lesson 23: Measuring Speed: timeit, cProfile and Memory

All runnable code from this lesson, combined in order.
"""

import timeit

setup = "data = list(range(10000)); s = set(data)"
t_list = timeit.timeit("9999 in data", setup=setup, number=2000)
t_set = timeit.timeit("9999 in s", setup=setup, number=2000)
print("set faster than list:", t_set < t_list)

t_loop = timeit.timeit("r=[]\nfor i in range(1000): r.append(i*i)", number=1000)
t_comp = timeit.timeit("[i*i for i in range(1000)]", number=1000)
print("comprehension no slower than loop:", t_comp <= t_loop * 1.2)

import tracemalloc
tracemalloc.start()
big = [i for i in range(100000)]
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("used over 1 MB:", peak > 1_000_000)


import cProfile, pstats, io

def slow():
    return sum(i * i for i in range(50000))

def fast():
    return 1

def main():
    slow(); fast()

pr = cProfile.Profile()
pr.enable(); main(); pr.disable()
buf = io.StringIO()
stats = pstats.Stats(pr, stream=buf).sort_stats("cumulative")
names = [k[2] for k in stats.stats]
print("slow" in names, "fast" in names)


import time

ids = list(range(20000))
wanted = list(range(0, 20000, 2))

t = time.perf_counter()
hits_list = sum(1 for w in wanted if w in ids)
slow = time.perf_counter() - t

id_set = set(ids)
t = time.perf_counter()
hits_set = sum(1 for w in wanted if w in id_set)
fast = time.perf_counter() - t

print(hits_list == hits_set, fast < slow)


import time

def timed(fn, *a):
    t = time.perf_counter()
    r = fn(*a)
    return r, time.perf_counter() - t

r, secs = timed(sum, range(1000))
print(r, secs < 1)


import timeit
a = timeit.timeit("s=''\nfor i in range(2000): s+=str(i)", number=200)
b = timeit.timeit("''.join(str(i) for i in range(2000))", number=200)
print("join is fast:", b < a * 2)


import timeit
runs = timeit.repeat("sorted(range(1000, 0, -1))", repeat=5, number=200)
print(len(runs), min(runs) <= max(runs))


import timeit

def dup_slow(a):
    return any(a[i] == a[j] for i in range(len(a)) for j in range(i))

def dup_fast(a):
    return len(set(a)) != len(a)

data = list(range(1500))
t1 = timeit.timeit(lambda: dup_slow(data), number=1)
t2 = timeit.timeit(lambda: dup_fast(data), number=1)
print(dup_slow(data) == dup_fast(data), t2 < t1)
