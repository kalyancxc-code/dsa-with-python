# Lesson 47: Binary Search: Find Anything in O(log n)

*Part D: Data Structures and Algorithms*

## Summary
- The binary search idea and loop.
- Why the input must be sorted.
- Writing it without off-by-one bugs.
- Using `bisect` and searching on a rotated array.

## Complexity
Time O(log n). Space O(1) for the loop version (O(log n) if recursive).

## Coding questions
- Q1 (Easy): Classic search
- Q2 (Easy): Search insert position
- Q3 (Medium): Integer square root
- Q4 (Hard): Search in a rotated sorted array

## Recap
- Halve the range each time.
- Keep `lo`, `hi`, `mid` updates exact.
- Next: binary search variants and "search on the answer".

## Run
```bash
python solution.py
python -m pytest
```
