# Lesson 56: Topological Sort: Ordering Tasks with Dependencies

*Part D: Data Structures and Algorithms*

## Summary
- Directed acyclic graphs (DAGs).
- Kahn's algorithm (BFS with in-degrees).
- DFS-based topological sort.
- Detecting impossible orders (cycles).

## Complexity
O(V + E) time, O(V + E) space.

## Coding questions
- Q1 (Easy): In-degrees
- Q2 (Easy): Can all courses be finished?
- Q3 (Medium): Course schedule order
- Q4 (Hard): Alien dictionary

## Recap
- Dependencies become edges; Kahn's algorithm orders them.
- A shortfall in the result reveals a cycle.
- Next: union-find.

## Run
```bash
python solution.py
python -m pytest
```
