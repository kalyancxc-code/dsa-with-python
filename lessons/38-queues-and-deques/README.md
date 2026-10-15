# Lesson 38: Queues and Deques: First In, First Out

*Part D: Data Structures and Algorithms*

## Summary
- What a queue is (FIFO) and its operations.
- Why `list.pop(0)` is slow and `deque` is fast.
- Circular queue (ring buffer).
- Queue using two stacks, and the sliding window maximum with a deque.

## Complexity
Queue and deque operations at the ends: O(1). Indexing into the middle of a deque: O(n).

## Coding questions
- Q1 (Easy): Recent counter (calls in the last 3000 ms)
- Q2 (Easy): Queue using two stacks
- Q3 (Medium): Rotate a deque / Josephus game
- Q4 (Hard): Sliding window maximum

## Recap
- Queue = FIFO; use `deque` in Python.
- Circular queues reuse space.
- Monotonic deques give O(n) window maximum.
- Next: monotonic stack.

## Run
```bash
python solution.py
python -m pytest
```
