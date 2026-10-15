# Lesson 46: Counting Sort and Python's Built-in Sort

*Part D: Data Structures and Algorithms*

## Summary
- Counting sort for small integer ranges.
- Radix sort idea (brief).
- Python's `sorted`, `key`, `reverse` and Timsort.
- Sorting by multiple fields.

## Complexity
| Sort | Time | Space |
|---|---|---|
| Counting | O(n + k) | O(k) |
| Timsort (`sorted`) | O(n log n) worst, O(n) best | O(n) |

## Coding questions
- Q1 (Easy): Sort strings by length
- Q2 (Easy): Sort a dict by value
- Q3 (Medium): Sort an array of 0s, 1s and 2s with counting
- Q4 (Hard): Maximum gap using buckets / sort then scan

## Recap
- Counting sort is linear when the range is small.
- Use `sorted` with `key` in real code.
- Next: binary search.

## Run
```bash
python solution.py
python -m pytest
```
