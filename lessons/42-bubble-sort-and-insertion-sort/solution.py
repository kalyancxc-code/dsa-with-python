"""Lesson 42: Bubble Sort and Insertion Sort: Your First Sorting Algorithms

All runnable code from this lesson, combined in order.
"""

def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:           # already sorted: stop early
            break
    return a

def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

data = [5, 2, 9, 1, 5, 6]
print(bubble_sort(data), insertion_sort(data), data)


a = [4, 3, 2, 1]
for i in range(1, len(a)):
    key, j = a[i], i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]; j -= 1
    a[j + 1] = key
    print("after inserting item", i, ":", a)


board = [98, 90, 85, 70, 60]
new = 88
board.append(new)
j = len(board) - 2
while j >= 0 and board[j] < new:      # descending order
    board[j + 1] = board[j]; j -= 1
board[j + 1] = new
print(board)


def selection_sort(a):
    a = a[:]
    for i in range(len(a)):
        m = min(range(i, len(a)), key=lambda k: a[k])
        a[i], a[m] = a[m], a[i]
    return a
print(selection_sort([64, 25, 12, 22, 11]))


def is_sorted(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))
print(is_sorted([1, 2, 2, 5]), is_sorted([3, 1]), is_sorted([]))


def count_swaps(a):
    a, swaps = a[:], 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps
print(count_swaps([3, 2, 1]), count_swaps([1, 2, 3]), count_swaps([2, 3, 1]))


def sort_colors(a):
    lo, mid, hi = 0, 0, len(a) - 1
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]; hi -= 1
    return a
print(sort_colors([2, 0, 2, 1, 1, 0]))
