"""Lesson 52: Heaps and Priority Queues: Always Get the Most Important Item

All runnable code from this lesson, combined in order.
"""

import heapq

h = []
for x in (5, 1, 8, 3, 9, 2):
    heapq.heappush(h, x)
print(h[0], heapq.heappop(h), heapq.heappop(h), h[0])

def k_largest(nums, k):
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return sorted(heap, reverse=True)

print(k_largest([3, 2, 1, 5, 6, 4], 2))

tasks = []
heapq.heappush(tasks, (2, "write report"))
heapq.heappush(tasks, (1, "fix outage"))
heapq.heappush(tasks, (3, "lunch"))
while tasks:
    print(heapq.heappop(tasks))


import heapq, itertools

counter = itertools.count()          # tie-breaker keeps order stable
q = []
def add(priority, name):
    heapq.heappush(q, (priority, next(counter), name))
add(2, "password reset"); add(1, "site down"); add(2, "invoice query"); add(1, "payment failure")
print([heapq.heappop(q)[2] for _ in range(4)])


import heapq
def last_stone(stones):
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) > 1:
        a, b = heapq.heappop(h), heapq.heappop(h)
        if a != b:
            heapq.heappush(h, a - b)
    return -h[0] if h else 0
print(last_stone([2, 7, 4, 1, 8, 1]))


import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k, self.h = k, []
        for x in nums: self.add(x)
    def add(self, x):
        heapq.heappush(self.h, x)
        if len(self.h) > self.k: heapq.heappop(self.h)
        return self.h[0]
kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3), kl.add(5), kl.add(10), kl.add(9))


import heapq
from collections import Counter
def top_k_words(words, k):
    counts = Counter(words)
    return heapq.nsmallest(k, counts, key=lambda w: (-counts[w], w))
print(top_k_words(["i", "love", "code", "i", "love", "dsa", "i"], 2))


import heapq
class MedianFinder:
    def __init__(self):
        self.low, self.high = [], []          # low is a max-heap (negated)
    def add(self, x):
        heapq.heappush(self.low, -x)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2

m = MedianFinder()
for x in (5, 15, 1, 3):
    m.add(x)
    print(x, "->", m.median())
