# Lesson 58: Dijkstra's Algorithm: Shortest Paths with Weights

*Part D: Data Structures and Algorithms*

## Summary
- Weighted graphs and why BFS isn't enough.
- Dijkstra with a min-heap.
- Reconstructing the path.
- Why negative weights break it.

## Complexity
With a heap: O((V + E) log V). Space O(V + E).

## Coding questions
- Q1 (Easy): Why BFS fails on weights
- Q2 (Easy): Network delay time
- Q3 (Medium): Cheapest path with at most k stops (Bellman-Ford style)
- Q4 (Hard): Path with minimum effort in a grid

## Recap
- Always expand the closest unfinished node.
- Heap + stale check = clean code.
- Next: minimum spanning trees.

## Run
```bash
python solution.py
python -m pytest
```
