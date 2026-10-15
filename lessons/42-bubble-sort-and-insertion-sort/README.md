# Lesson 42: Bubble Sort and Insertion Sort: Your First Sorting Algorithms

*Part D: Data Structures and Algorithms*

## Summary
- Bubble sort and its early-exit trick.
- Insertion sort and why it shines on nearly sorted data.
- Selection sort for comparison.
- Stability and in-place sorting.

## Complexity
| Sort | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble (early exit) | O(n) | O(n²) | O(n²) | O(1) | yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | no |

## Coding questions
- Q1 (Easy): Selection sort
- Q2 (Easy): Is the list sorted?
- Q3 (Medium): Count swaps in bubble sort
- Q4 (Hard): Sort colours (0, 1, 2) in one pass

## Recap
- Bubble and insertion sorts are simple, O(n²).
- Insertion sort is great for nearly sorted input.
- Next: merge sort, which is much faster.

## Run
```bash
python solution.py
python -m pytest
```
