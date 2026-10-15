# Lesson 29: Two Pointers: Solve Pair Problems in One Pass

*Part D: Data Structures and Algorithms*

## Summary
- Opposite-direction pointers (start and end).
- Same-direction pointers (slow and fast).
- When the pattern applies (sorted data or in-place work).
- Classic problems: pair sum, 3Sum, container with most water, palindrome.

## Complexity
O(n) time (each pointer moves at most n steps), O(1) space. Sorting first adds O(n log n).

## Coding questions
- Q1 (Easy): Valid palindrome
- Q2 (Easy): Squares of a sorted array, sorted
- Q3 (Medium): Container with most water
- Q4 (Hard): 3Sum

## Recap
- Two pointers replace nested loops on sorted data.
- Each move discards impossible options.
- Next: sliding window.

## Run
```bash
python solution.py
python -m pytest
```
