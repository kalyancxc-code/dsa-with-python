# Lesson 45: Heap Sort: Sorting with a Heap

*Part D: Data Structures and Algorithms*

## Summary
- What a binary heap is and how it lives inside an array.
- Sift-down (heapify) and building a heap in O(n).
- Heap sort step by step.
- Complexity: O(n log n) time, O(1) extra space, not stable.

## Complexity
Build heap: O(n). Then n times sift-down at O(log n). Total O(n log n) in all cases. Extra space O(1). Not stable.

## Coding questions
- Q1 (Easy): Parent and child indexes
- Q2 (Easy): Is a list a valid max-heap?
- Q3 (Medium): Sort descending with heapq
- Q4 (Hard): Sort a nearly sorted list (each item is at most k away)

## Recap
- Heap in an array; sift down to fix order.
- Build, swap root with end, shrink, repeat.
- Next: counting sort and Python's sort.

## Run
```bash
python solution.py
python -m pytest
```
