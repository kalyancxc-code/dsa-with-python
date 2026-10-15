"""Lesson 66: Intervals: Merge, Insert and Schedule

All runnable code from this lesson, combined in order.
"""

def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1, 3], [8, 10], [2, 6], [15, 18], [17, 20]]))
print(merge_intervals([[1, 4], [4, 5]]), merge_intervals([]))


bookings = [[9, 11], [10, 12], [14, 15], [14.5, 16]]
merged = []
for s, e in sorted(bookings):
    if merged and s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])
print(merged, sum(e - s for s, e in merged))


def can_attend(intervals):
    intervals = sorted(intervals)
    return all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:]))
print(can_attend([[0, 30], [5, 10], [15, 20]]), can_attend([[7, 10], [2, 4]]))


def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]
print(overlap([1, 5], [4, 8]), overlap([1, 2], [3, 4]), overlap([1, 3], [3, 4]))


def insert(intervals, new):
    out, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:
        out.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:
        new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]; i += 1
    out.append(new)
    out.extend(intervals[i:])
    return out
print(insert([[1, 3], [6, 9]], [2, 5]), insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


import heapq

def min_rooms(intervals):
    heap = []                                   # end times of rooms in use
    for s, e in sorted(intervals):
        if heap and heap[0] <= s:
            heapq.heapreplace(heap, e)          # reuse a free room
        else:
            heapq.heappush(heap, e)             # need a new room
    return len(heap)

def min_rooms_sweep(intervals):
    events = sorted([(s, 1) for s, e in intervals] + [(e, -1) for s, e in intervals])
    cur = best = 0
    for _, d in events:
        cur += d
        best = max(best, cur)
    return best

m = [[0, 30], [5, 10], [15, 20]]
print(min_rooms(m), min_rooms_sweep(m), min_rooms([[7, 10], [2, 4]]))
