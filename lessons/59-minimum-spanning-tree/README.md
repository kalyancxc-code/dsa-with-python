# Lesson 59: Minimum Spanning Tree: Kruskal and Prim

*Part D: Data Structures and Algorithms*

## Summary
- What a spanning tree and an MST are.
- Kruskal's algorithm (sort edges + union-find).
- Prim's algorithm (grow from a node with a heap).
- When to use each.

## Complexity
Kruskal: O(E log E) for sorting. Prim with a heap: O(E log V). Both give the same total weight.

## Coding questions
- Q1 (Easy): Count edges in an MST
- Q2 (Easy): Is the graph connected? (can an MST exist)
- Q3 (Medium): Min cost to connect points (Manhattan distance)
- Q4 (Hard): MST cost after removing each edge

## Recap
- Connect everything with the least total weight.
- Kruskal = sort + union-find; Prim = grow + heap.
- Next: dynamic programming.

## Run
```bash
python solution.py
python -m pytest
```
