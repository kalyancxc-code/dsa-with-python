# Lesson 69: Capstone and Mock Interview 2: Build a Mini Route Planner

*Part D: Data Structures and Algorithms*

## Summary
- Combining several data structures in one design.
- Choosing the right structure for each feature and justifying it.
- Handling follow-up questions on scale and edge cases.
- Presenting complexity for the whole system.

## Complexity
| Feature | Time |
|---|---|
| Connected check | near O(1) |
| Autocomplete | O(L + results) |
| Route (miss) | O((V+E) log V) |
| Route (hit) | O(1) |

## Coding questions
- Q1 (Easy): Minutes to hours and minutes label
- Q2 (Easy): Direct neighbours of a place
- Q3 (Medium): Count how many separate road networks exist
- Q4 (Hard): Find the best meeting point (minimise the farthest travel time)

## Recap
- Real systems combine structures; each one has a clear job.
- Explain choices and complexity.
- Next: your pattern cheat sheet and what to do after this course.

## Run
```bash
python solution.py
python -m pytest
```
