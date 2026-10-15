# Lesson 61: Dynamic Programming 2: Grids and 2D Tables

*Part D: Data Structures and Algorithms*

## Summary
- 2D states: `dp[row][col]`.
- Counting paths, minimum path sum, obstacles.
- Edit distance (a classic).
- Reducing 2D tables to one row.

## Complexity
2D table: O(m·n) time and space; one row: O(m·n) time, O(n) space.

## Coding questions
- Q1 (Easy): Unique paths with obstacles
- Q2 (Easy): Pascal's triangle row
- Q3 (Medium): Maximal square of 1s
- Q4 (Hard): Edit distance

## Recap
- 2D state = two indexes.
- Fill in dependency order; handle borders.
- Next: knapsack.

## Run
```bash
python solution.py
python -m pytest
```
