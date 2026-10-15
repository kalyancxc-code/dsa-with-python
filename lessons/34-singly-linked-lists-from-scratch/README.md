# Lesson 34: Singly Linked Lists from Scratch

*Part D: Data Structures and Algorithms*

## Summary
- Nodes and the head pointer.
- Insert at head and tail, delete by value, search.
- Why access is O(n) but insert at head is O(1).
- Dummy-node technique.

## Complexity
| Operation | Time |
|---|---|
| push_front | O(1) |
| push_back (no tail pointer) | O(n) |
| find / delete by value | O(n) |
Space: O(n) for n nodes.

## Coding questions
- Q1 (Easy): Build a list from an array and print it
- Q2 (Easy): Length of a list
- Q3 (Medium): Remove the nth node from the end
- Q4 (Hard): Merge two sorted linked lists

## Recap
- Nodes link by `next`.
- Fast at the head, slow to search.
- Dummy node and two pointers are your two best friends.
- Next: doubly linked lists.

## Run
```bash
python solution.py
python -m pytest
```
