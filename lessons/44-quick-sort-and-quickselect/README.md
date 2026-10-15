# Lesson 44: Quick Sort and Quickselect

*Part D: Data Structures and Algorithms*

## Summary
- Partitioning around a pivot.
- Quick sort average and worst case.
- Choosing a good pivot (random).
- Quickselect for the k-th largest.

## Complexity
| Case | Time |
|---|---|
| Best / average | O(n log n) |
| Worst (bad pivots) | O(n²) |
Space: O(log n) stack for in-place (average). Not stable.

## Coding questions
- Q1 (Easy): Partition around a pivot value
- Q2 (Easy): Sort descending with quick sort
- Q3 (Medium): K-th largest element
- Q4 (Hard): Count how quick sort degrades

## Recap
- Partition around a pivot, then recurse.
- Random pivots avoid the O(n²) trap.
- Quickselect gives k-th element in O(n) average.
- Next: heap sort.

## Run
```bash
python solution.py
python -m pytest
```
