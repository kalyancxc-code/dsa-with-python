# Lesson 33: Hash Sets and How Hashing Really Works

*Part D: Data Structures and Algorithms*

## Summary
- How a hash table stores items (buckets, collisions).
- Why keys must be immutable and hashable.
- Hash sets for membership, uniqueness and intersections.
- Building a tiny hash table yourself.

## Complexity
Average O(1) for put, get and remove. Worst case O(n) if all keys collide. Resize is O(n) but rare, so amortized O(1).

## Coding questions
- Q1 (Easy): Intersection of two arrays
- Q2 (Easy): Happy number
- Q3 (Medium): Longest consecutive sequence
- Q4 (Hard): Design a set with add, remove, contains

## Recap
- Hash, mod, bucket; chain on collision; resize when crowded.
- Sets give fast membership and uniqueness.
- Next: linked lists.

## Run
```bash
python solution.py
python -m pytest
```
