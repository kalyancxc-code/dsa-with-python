# Lesson 36: Reverse a Linked List and Detect Cycles

*Part D: Data Structures and Algorithms*

## Summary
- Reversing iteratively (three pointers) and recursively.
- Floyd's cycle detection (slow and fast pointers).
- Finding where a cycle starts.
- Finding the middle of a list and checking for a palindrome.

## Complexity
Reverse: O(n) time, O(1) space. Cycle detection: O(n) time, O(1) space (a set of visited nodes would need O(n)).

## Coding questions
- Q1 (Easy): Middle of the list
- Q2 (Easy): Recursive reverse
- Q3 (Medium): Where does the cycle start?
- Q4 (Hard): Is the list a palindrome? (O(1) space)

## Recap
- Reverse with prev/cur/nxt.
- Tortoise and hare find loops.
- Next: stacks.

## Run
```bash
python solution.py
python -m pytest
```
