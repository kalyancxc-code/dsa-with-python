# Lesson 9: Sets and Dictionaries: Fast Lookup Tools

*Part A: Python Foundations*

## Summary
- Dictionaries: key-value pairs, get, items, update.
- Sets: unique values and set maths.
- Why lookup is O(1) on average.
- Counting and grouping patterns.

## Complexity
| Operation | Average | Worst |
|---|---|---|
| get / set / `in` on dict or set | O(1) | O(n) |
| iterate | O(n) | O(n) |

## Coding questions
- Q1 (Easy): Does a list have duplicates?
- Q2 (Easy): Count words
- Q3 (Medium): Group words by first letter
- Q4 (Hard): First non-repeating character

## Recap
- Dict = key to value; set = unique items.
- Both give O(1) average lookup.
- Use them to remove nested loops.
- Next: comprehensions.

## Run
```bash
python solution.py
python -m pytest
```
