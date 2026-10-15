# Lesson 31: Prefix Sums: Answer Range Queries in O(1)

*Part D: Data Structures and Algorithms*

## Summary
- Building a prefix sum array.
- Range sum in O(1).
- Subarray-sum-equals-k using a hash map.
- 2D prefix sums (idea).

## Complexity
Build: O(n) time, O(n) space. Each query: O(1). Without prefix sums, each query is O(n).

## Coding questions
- Q1 (Easy): Range sum query (immutable)
- Q2 (Easy): Pivot index (left sum equals right sum)
- Q3 (Medium): Subarray sum equals k
- Q4 (Hard): 2D range sum

## Recap
- Prefix sums precompute running totals.
- Subtract to get any range in O(1).
- With a hash map they count subarrays with a target sum.
- Next: hash maps.

## Run
```bash
python solution.py
python -m pytest
```
