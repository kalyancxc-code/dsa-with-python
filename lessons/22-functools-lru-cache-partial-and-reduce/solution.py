"""Lesson 22: functools: lru_cache, partial and reduce

All runnable code from this lesson, combined in order.
"""

from functools import lru_cache, partial, reduce, cache

calls = 0

def slow_fib(n):
    global calls
    calls += 1
    return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)

slow_fib(25)
print("calls without cache:", calls)

@lru_cache(maxsize=None)
def fast_fib(n):
    return n if n < 2 else fast_fib(n - 1) + fast_fib(n - 2)

print(fast_fib(25), fast_fib(90))
print(fast_fib.cache_info())

pow2 = partial(pow, 2)
print(pow2(10))

print(reduce(lambda a, b: a * b, [1, 2, 3, 4, 5]))

@cache
def grid_paths(r, c):
    if r == 0 or c == 0:
        return 1
    return grid_paths(r - 1, c) + grid_paths(r, c - 1)
print(grid_paths(10, 10))


from functools import lru_cache

hits = {"slow": 0}

@lru_cache(maxsize=128)
def tax_for(region):
    hits["slow"] += 1
    return {"IN": 0.18, "US": 0.07}.get(region, 0.0)

for r in ["IN", "US", "IN", "IN", "US"]:
    tax_for(r)
print("slow calls:", hits["slow"])


from functools import lru_cache

@lru_cache(maxsize=None)
def sq(n):
    return n * n

print(sq(12), sq(12), sq.cache_info().hits)


from functools import reduce
print(reduce(lambda a, b: a * b, range(1, 6)))


from functools import lru_cache

@lru_cache(maxsize=None)
def stairs(n):
    if n <= 2:
        return n
    return stairs(n - 1) + stairs(n - 2)

print([stairs(i) for i in range(1, 8)], stairs(40))


from functools import cmp_to_key

def largest_number(nums):
    def cmp(a, b):
        return -1 if a + b > b + a else 1
    strs = sorted(map(str, nums), key=cmp_to_key(cmp))
    return str(int("".join(strs)))

print(largest_number([3, 30, 34, 5, 9]))
