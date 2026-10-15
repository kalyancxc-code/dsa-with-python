# Lesson 64: Longest Increasing Subsequence (LIS): O(n²) and O(n log n)

*Part D: Data Structures and Algorithms*

## Summary
- The O(n²) DP.
- The O(n log n) "patience" method with `bisect`.
- Variants: number of LIS, longest non-decreasing, envelopes.
- Reconstructing the sequence.

## Complexity
DP: O(n²) time, O(n) space. Tails with binary search: O(n log n) time, O(n) space.

## Coding questions
- Q1 (Easy): Length of the longest non-decreasing run (continuous)
- Q2 (Easy): LIS length (fast)
- Q3 (Medium): Reconstruct one LIS
- Q4 (Hard): Number of longest increasing subsequences

## Recap
- Two ways: O(n²) DP, O(n log n) tails.
- Reconstruct with a predecessor array.
- Next: greedy.

## Run
```bash
python solution.py
python -m pytest
```
