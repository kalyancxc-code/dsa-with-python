# Lesson 32: Hash Maps: Count, Group and Look Up in O(1)

*Part D: Data Structures and Algorithms*

## Summary
- Using a dictionary as a counter, a lookup table and a grouping tool.
- The "complement" pattern (Two Sum).
- Grouping anagrams and finding top frequent items.
- Hash map cost and trade-offs.

## Complexity
Average O(1) per insert or lookup, so one pass is O(n). Space is O(n) for stored keys. Grouping words costs O(n · k log k) for word length k.

## Coding questions
- Q1 (Easy): Two Sum
- Q2 (Easy): Isomorphic strings
- Q3 (Medium): Top k frequent elements
- Q4 (Hard): Count subarrays divisible by k

## Recap
- Counting, complement and grouping cover most hash map problems.
- O(1) average lookup, O(n) space.
- Next: sets and how hashing works inside.

## Run
```bash
python solution.py
python -m pytest
```
