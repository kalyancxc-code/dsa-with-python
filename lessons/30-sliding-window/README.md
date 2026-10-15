# Lesson 30: Sliding Window: Fast Subarray and Substring Answers

*Part D: Data Structures and Algorithms*

## Summary
- Fixed-size windows.
- Variable-size windows that grow and shrink.
- Tracking window state with sums, sets and counters.
- Classic problems: max sum of k, longest unique substring, minimum window.

## Complexity
Each index enters and leaves the window at most once, so time is O(n). Space is O(1) for sums, or O(k) for the set or counter.

## Coding questions
- Q1 (Easy): Average of every window of size k
- Q2 (Easy): Contains nearby duplicate (within k)
- Q3 (Medium): Smallest subarray with sum at least target
- Q4 (Hard): Minimum window substring

## Recap
- Slide, add, remove, update.
- Variable windows expand then shrink.
- Next: prefix sums.

## Run
```bash
python solution.py
python -m pytest
```
