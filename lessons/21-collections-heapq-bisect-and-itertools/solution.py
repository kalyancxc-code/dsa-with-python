"""Lesson 21: collections, heapq, bisect and itertools: The Interview Toolbox

All runnable code from this lesson, combined in order.
"""

from collections import Counter, defaultdict, deque
import heapq, bisect, itertools

print(Counter("abracadabra").most_common(2))

groups = defaultdict(list)
for w in ["tea", "ten", "cat", "car"]:
    groups[w[0]].append(w)
print(dict(groups))

d = deque([1, 2, 3])
d.appendleft(0); d.append(4)
print(d, d.popleft(), d.pop(), d)

h = [5, 1, 8, 3]
heapq.heapify(h)
print(heapq.heappop(h), heapq.nsmallest(2, [9, 4, 7, 1]), heapq.nlargest(2, [9, 4, 7, 1]))

arr = [10, 20, 20, 30]
print(bisect.bisect_left(arr, 20), bisect.bisect_right(arr, 20))
bisect.insort(arr, 25)
print(arr)

print(list(itertools.permutations([1, 2, 3], 2)))
print(list(itertools.combinations("abc", 2)))
print(list(itertools.product([0, 1], repeat=2)))
print(list(itertools.accumulate([1, 2, 3, 4])))
print([(k, len(list(g))) for k, g in itertools.groupby("aaabbc")])


from collections import Counter

visits = ["home", "cart", "home", "pay", "home", "cart", "help"]
print(Counter(visits).most_common(3))


from collections import Counter
print(sorted(Counter("hello").items()))


import heapq
print(heapq.nsmallest(3, [7, 2, 9, 1, 5, 3]))


import bisect

def grade(score, cuts=(60, 75, 90), names="DCBA"):
    return names[bisect.bisect(cuts, score)]

print([grade(s) for s in (50, 60, 80, 95)])


from collections import deque

def last_k(stream, k):
    window = deque(maxlen=k)
    for x in stream:
        window.append(x)
        yield list(window)

print(list(last_k([1, 2, 3, 4, 5], 3))[-2:])
