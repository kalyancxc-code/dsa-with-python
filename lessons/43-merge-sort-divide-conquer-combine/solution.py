"""Lesson 43: Merge Sort: Divide, Conquer, Combine

All runnable code from this lesson, combined in order.
"""

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(left, right)

def merge(left, right):
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:          # <= keeps it stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

print(merge([3, 6], [2, 8]))
print(merge_sort([6, 3, 8, 2, 9, 1, 5]))
print(merge_sort([]), merge_sort([7]))


import heapq
store_a = [100, 250, 400]
store_b = [50, 300, 450, 600]
print(list(heapq.merge(store_a, store_b)))


def merge(a, b):
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 4, 7], [2, 3, 9, 10]))


people = [("Asha", 30), ("Ravi", 25), ("Meera", 30), ("Zoya", 25)]
print(sorted(people, key=lambda p: p[1]))


def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, x = count_inversions(a[:mid])
    right, y = count_inversions(a[mid:])
    merged, i, j, z = [], 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            z += len(left) - i          # all remaining left items are bigger
    merged += left[i:] + right[j:]
    return merged, x + y + z

print(count_inversions([2, 4, 1, 3, 5])[1], count_inversions([5, 4, 3, 2, 1])[1])


import heapq

def merge_k(lists):
    heap = [(l[0], i, 0) for i, l in enumerate(lists) if l]
    heapq.heapify(heap)
    out = []
    while heap:
        val, i, j = heapq.heappop(heap)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out
print(merge_k([[1, 4, 5], [1, 3, 4], [2, 6]]))
