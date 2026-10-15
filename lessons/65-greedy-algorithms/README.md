# Lesson 65: Greedy Algorithms: Make the Best Choice Now

*Part D: Data Structures and Algorithms*

## Summary
- The greedy idea and when it works.
- Proving a greedy choice (exchange argument, simply).
- Classic problems: activity selection, jump game, gas station, assign cookies.
- When greedy fails and DP is needed.

## Complexity
Typically O(n log n) because of the initial sort, then O(n).

## Coding questions
- Q1 (Easy): Assign cookies
- Q2 (Easy): Jump game (can you reach the end?)
- Q3 (Medium): Minimum jumps to reach the end
- Q4 (Hard): Gas station

## Recap
- Pick the best choice now; prove or test it.
- Sort first, then sweep.
- Fall back to DP when greedy breaks.
- Next: intervals.

## Run
```bash
python solution.py
python -m pytest
```
