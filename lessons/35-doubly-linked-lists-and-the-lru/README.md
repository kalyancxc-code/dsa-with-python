# Lesson 35: Doubly Linked Lists and the LRU Cache

*Part D: Data Structures and Algorithms*

## Summary
- Nodes with `prev` and `next`.
- O(1) delete when you hold the node.
- Sentinel (dummy) head and tail.
- Building an LRU cache with a dict plus a doubly linked list.

## Complexity
`get` and `put` are O(1). Space is O(capacity).

## Coding questions
- Q1 (Easy): Build and print forwards and backwards
- Q2 (Easy): Delete a given node in O(1)
- Q3 (Medium): Browser history
- Q4 (Hard): LFU-lite: count uses, evict the least used

## Recap
- Two-way links give O(1) removal.
- LRU = dict + doubly linked list.
- Next: reversing and cycle detection.

## Run
```bash
python solution.py
python -m pytest
```
