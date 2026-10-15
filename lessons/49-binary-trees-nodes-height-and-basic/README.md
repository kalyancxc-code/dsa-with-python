# Lesson 49: Binary Trees: Nodes, Height and Basic Properties

*Part D: Data Structures and Algorithms*

## Summary
- Tree vocabulary: root, parent, child, leaf, depth, height.
- Building a binary tree with nodes.
- Recursive thinking on trees.
- Height, size, symmetry, path sums.

## Complexity
Each node is visited once: O(n) time. Space is O(h) for the recursion, where h is the height: O(log n) for a balanced tree and O(n) for a skewed one.

## Coding questions
- Q1 (Easy): Maximum depth
- Q2 (Easy): Invert a binary tree
- Q3 (Medium): Is the tree symmetric?
- Q4 (Hard): Diameter of a binary tree

## Recap
- Trees are recursive: solve left, solve right, combine.
- Height, size, leaves, symmetry, diameter all use the same shape.
- Next: tree traversals.

## Run
```bash
python solution.py
python -m pytest
```
