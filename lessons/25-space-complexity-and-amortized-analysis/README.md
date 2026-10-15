# Lesson 25: Space Complexity and Amortized Analysis

*Part C: Complexity and Problem Solving*

## Summary
- What space complexity is, including the call stack.
- Auxiliary space vs input space.
- Time-space trade-offs.
- Amortized analysis: why `list.append` is O(1) on average.

## Complexity
| Pattern | Time | Extra space |
|---|---|---|
| Single pass with counters | O(n) | O(1) |
| Hash set of seen items | O(n) | O(n) |
| Recursion depth n | varies | O(n) stack |
| Two pointers in place | O(n) | O(1) |

## Coding questions
- Q1 (Easy): Space of a running max
- Q2 (Easy): Space of building a new list
- Q3 (Medium): Recursion space of factorial
- Q4 (Hard): Amortized cost of a dynamic array

## Recap
- Count extra memory, including the call stack.
- Amortized O(1) is average cost over time.
- Offer trade-offs in interviews.
- Next: how to approach a problem.

## Run
```bash
python solution.py
python -m pytest
```
