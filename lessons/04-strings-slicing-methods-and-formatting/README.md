# Lesson 4: Strings: Slicing, Methods and Formatting

*Part A: Python Foundations*

## Summary
- Indexing and slicing, including negative indexes.
- Common string methods: split, join, strip, replace, find.
- f-strings for formatting.
- Why strings are immutable and what that costs.

## Complexity
- Index: O(1). Slice: O(k) for k characters copied. `in` / `find`: O(n·m) worst case. `join`: O(total length).
- Repeated `s += x` in a loop: O(n²) in the worst case.

## Coding questions
- Q1 (Easy): Reverse a string
- Q2 (Easy): Count vowels
- Q3 (Medium): Valid palindrome (ignore case and symbols)
- Q4 (Hard): Are two strings anagrams?

## Recap
- Index from 0; slice with start:stop:step.
- Strings are immutable; use join for building.
- Counter and slicing solve many classic problems.
- Next: conditionals.

## Run
```bash
python solution.py
python -m pytest
```
