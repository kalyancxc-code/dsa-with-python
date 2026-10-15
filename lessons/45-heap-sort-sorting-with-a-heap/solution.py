"""Lesson 45: Heap Sort: Sorting with a Heap

All runnable code from this lesson, combined in order.
"""

def sift_down(a, i, n):
    while True:
        largest, l, r = i, 2 * i + 1, 2 * i + 2
        if l < n and a[l] > a[largest]: largest = l
        if r < n and a[r] > a[largest]: largest = r
        if largest == i:
            return
        a[i], a[largest] = a[largest], a[i]
        i = largest

def heap_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):      # build heap in O(n)
        sift_down(a, i, n)
    print("max-heap:", a)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]          # move max to its place
        sift_down(a, 0, end)
    return a

print(heap_sort([30, 60, 50, 90, 70, 80]))


readings = [42, 7, 19, 88, 3, 56]
def hs(a):
    n = len(a)
    def sd(i, n):
        while 2 * i + 1 < n:
            c = 2 * i + 1
            if c + 1 < n and a[c + 1] > a[c]: c += 1
            if a[i] >= a[c]: break
            a[i], a[c] = a[c], a[i]; i = c
    for i in range(n // 2 - 1, -1, -1): sd(i, n)
    for e in range(n - 1, 0, -1):
        a[0], a[e] = a[e], a[0]; n = e; sd(0, n)
    return a
print(hs(readings))


i = 4
print("parent:", (i - 1) // 2, "children:", 2 * i + 1, 2 * i + 2)


def is_max_heap(a):
    return all(a[i] >= a[c] for i in range(len(a)) for c in (2*i+1, 2*i+2) if c < len(a))
print(is_max_heap([90, 70, 80, 30, 60, 50]), is_max_heap([10, 20, 5]))


import heapq
a = [5, 1, 9, 3, 7]
h = [-x for x in a]
heapq.heapify(h)
print([-heapq.heappop(h) for _ in range(len(a))])


import heapq

def sort_k_sorted(a, k):
    h = a[:k + 1]
    heapq.heapify(h)
    out = []
    for x in a[k + 1:]:
        out.append(heapq.heappushpop(h, x))
    while h:
        out.append(heapq.heappop(h))
    return out
print(sort_k_sorted([6, 5, 3, 2, 8, 10, 9], 3))
