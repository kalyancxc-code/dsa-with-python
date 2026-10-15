# Lesson 57: Union-Find (Disjoint Set Union): Track Groups Fast

*Part D: Data Structures and Algorithms*

## Summary
- The two operations: find and union.
- Path compression and union by rank.
- Counting components and detecting cycles.
- Accounts merge and redundant connection style problems.

## Complexity
find and union: almost O(1) amortized (O(α(n))). Space O(n).

## Coding questions
- Q1 (Easy): Are two nodes connected?
- Q2 (Easy): Number of provinces
- Q3 (Medium): Redundant connection (the edge that forms a cycle)
- Q4 (Hard): Accounts merge

## Recap
- Find the leader; union merges groups.
- Compress paths, union by size.
- Next: Dijkstra's shortest path.

## Run
```bash
python solution.py
python -m pytest
```
