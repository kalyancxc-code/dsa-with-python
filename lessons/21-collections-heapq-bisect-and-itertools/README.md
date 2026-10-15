# Lesson 21: collections, heapq, bisect and itertools: The Interview Toolbox

*Part B: Advanced Python*

## Summary
- `Counter`, `defaultdict`, `deque`, `OrderedDict`.
- `heapq` for min-heaps and top-k.
- `bisect` for sorted lists.
- `itertools`: `permutations`, `combinations`, `product`, `accumulate`, `groupby`.

## Complexity
| Tool | Key operation | Time |
|---|---|---|
| `deque` | append/pop both ends | O(1) |
| `heapq` | push / pop | O(log n) |
| `heapq.heapify` | build | O(n) |
| `bisect` | search | O(log n) |
| `bisect.insort` | insert | O(n) (shifting) |
| `Counter` | count | O(n) |

## Coding questions
- Q1 (Easy): Letter frequencies
- Q2 (Easy): Smallest 3 numbers
- Q3 (Medium): Where would a score be inserted?
- Q4 (Hard): Sliding window of last k items

## Recap
- Counter, deque, heapq, bisect and itertools cover most needs.
- Know their costs.
- Next: functools and caching.

## Run
```bash
python solution.py
python -m pytest
```
