"""Lesson 33: Hash Sets and How Hashing Really Works

All runnable code from this lesson, combined in order.
"""

class MyHashMap:
    def __init__(self, size=8):
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _index(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1
        if self.count > 0.75 * len(self.buckets):
            self._resize()

    def get(self, key, default=None):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def _resize(self):
        old = [p for b in self.buckets for p in b]
        self.buckets = [[] for _ in range(len(self.buckets) * 2)]
        self.count = 0
        for k, v in old:
            self.put(k, v)

m = MyHashMap()
for i in range(10):
    m.put(i, i * i)
m.put(3, "three")
print(m.get(3), m.get(9), m.get(99, "none"), len(m.buckets), m.count)
print(m.remove(3), m.get(3), m.count)


taken = {"asha", "ravi", "meera"}
def register(name, taken):
    name = name.lower()
    if name in taken:
        return "taken"
    taken.add(name)
    return "ok"
print(register("Asha", taken), register("Zoya", taken), register("zoya", taken))


def intersection(a, b):
    return sorted(set(a) & set(b))
print(intersection([1, 2, 2, 1], [2, 2, 3]))


def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
print(is_happy(19), is_happy(2))


def longest_run(nums):
    s, best = set(nums), 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
    return best
print(longest_run([100, 4, 200, 1, 3, 2]), longest_run([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


class MySet:
    def __init__(self):
        self.buckets = [[] for _ in range(16)]
    def _b(self, x):
        return self.buckets[hash(x) % 16]
    def add(self, x):
        b = self._b(x)
        if x not in b:
            b.append(x)
    def remove(self, x):
        b = self._b(x)
        if x in b:
            b.remove(x)
    def contains(self, x):
        return x in self._b(x)

s = MySet()
s.add(1); s.add(17); s.add(1)
print(s.contains(1), s.contains(17), s.contains(2))
s.remove(1)
print(s.contains(1), s.contains(17))
