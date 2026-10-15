# Lesson 67: Bit Manipulation: Tricks with Zeros and Ones

*Part D: Data Structures and Algorithms*

## Summary
- Binary numbers and bitwise operators.
- Common tricks: check, set, clear, toggle a bit; count set bits; power of two.
- XOR properties for finding a single number.
- Bitmasks to represent subsets.

## Complexity
Most bit operations are O(1). Counting set bits with `n & (n-1)` takes O(number of 1-bits).

## Coding questions
- Q1 (Easy): Single number (others appear twice)
- Q2 (Easy): Power of two
- Q3 (Medium): Counting bits for 0..n
- Q4 (Hard): Missing number and two missing singles

## Recap
- Bits are switches; learn `& | ^ << >>`.
- XOR cancels pairs; `n & (n-1)` clears a bit.
- Next: the interview mock sessions.

## Run
```bash
python solution.py
python -m pytest
```
