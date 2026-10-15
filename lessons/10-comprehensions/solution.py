"""Lesson 10: Comprehensions: Short, Readable Loops

All runnable code from this lesson, combined in order.
"""

nums = [1, 2, 3, 4, 5, 6]
print([n * n for n in nums])
print([n for n in nums if n % 2 == 0])
print(["even" if n % 2 == 0 else "odd" for n in nums])
print({n % 3 for n in nums})
words = ["tea", "coffee", "milk"]
print({w: len(w) for w in words})
print([(i, j) for i in range(2) for j in range(2)])
matrix = [[1, 2], [3, 4], [5, 6]]
print([x for row in matrix for x in row])
print([list(col) for col in zip(*matrix)])
print(sum(n * n for n in nums))


orders = [120, 800, 560, 90, 1500]
print([round(a * 1.18, 2) for a in orders if a > 500])


print([n * n for n in range(10) if n % 2 == 0])


print([len(w) for w in "learn data structures well".split()])


def flatten(m):
    return [x for row in m for x in row]

def transpose(m):
    return [list(r) for r in zip(*m)]

m = [[1, 2, 3], [4, 5, 6]]
print(flatten(m), transpose(m))


def invert(d):
    out = {}
    for k, v in d.items():
        out.setdefault(v, []).append(k)
    return out

print(invert({"a": 1, "b": 2, "c": 1}))
print({v: k for k, v in {"x": 1, "y": 2}.items()})
