# Lesson 63: Longest Common Subsequence (LCS) and String DP

*Part D: Data Structures and Algorithms*

## Summary
- Subsequence vs substring.
- The LCS table and recurrence.
- Rebuilding the actual subsequence.
- Related: longest palindromic subsequence, shortest common supersequence, distinct subsequences.

## Complexity
Time O(m·n), space O(m·n) (O(min(m, n)) if you only need the length).

## Coding questions
- Q1 (Easy): Is s a subsequence of t?
- Q2 (Easy): Longest common substring (continuous)
- Q3 (Medium): Longest palindromic subsequence
- Q4 (Hard): Number of distinct subsequences of s equal to t

## Recap
- Two strings, two indexes, one table.
- Match goes diagonal; mismatch takes the better neighbour.
- Next: longest increasing subsequence.

## Run
```bash
python solution.py
python -m pytest
```
