# Lesson 52: Heaps and Priority Queues: Always Get the Most Important Item

*Part D: Data Structures and Algorithms*

## Summary
- Priority queue idea and min-heap vs max-heap.
- `heapq` operations: push, pop, peek, heapify.
- Top-k problems and why a heap of size k works.
- Running median with two heaps.

## Complexity
| Operation | Time |
|---|---|
| push / pop | O(log n) |
| peek top | O(1) |
| heapify list | O(n) |
| k largest of n | O(n log k) |

## Coding questions
- Q1 (Easy): Last stone weight
- Q2 (Easy): K-th largest in a stream
- Q3 (Medium): Top k frequent words
- Q4 (Hard): Median of a data stream (two heaps)

## Recap
- Heaps give fast access to the extreme item.
- Top-k and streaming medians are classic uses.
- Next: tries.

## Run
```bash
python solution.py
python -m pytest
```
