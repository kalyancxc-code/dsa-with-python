# Lesson 8: Lists and Tuples: Python's Workhorse Sequences

*Part A: Python Foundations*

## Summary
- Creating, indexing, slicing and changing lists.
- Core methods and their time cost.
- Tuples and when to use them.
- Sorting and copying lists.

## Complexity
| Operation | Time |
|---|---|
| `lst[i]`, `append`, `pop()` | O(1) |
| `insert`, `pop(0)`, `remove`, `in` | O(n) |
| `sort` | O(n log n) |
| slice of k items | O(k) |

## Coding questions
- Q1 (Easy): Largest and smallest
- Q2 (Easy): Remove duplicates, keep order
- Q3 (Medium): Rotate a list right by k
- Q4 (Hard): Second largest distinct value in one pass

## Recap
- Lists are fast at the end, slow at the front.
- Tuples are fixed and hashable.
- Beware shared inner lists.
- Next: sets and dicts.

## Run
```bash
python solution.py
python -m pytest
```
