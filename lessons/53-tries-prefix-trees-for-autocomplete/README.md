# Lesson 53: Tries: Prefix Trees for Autocomplete

*Part D: Data Structures and Algorithms*

## Summary
- What a trie is and how words share prefixes.
- Insert, search, starts-with.
- Autocomplete with DFS.
- Complexity and memory trade-offs.

## Complexity
Insert, search and starts-with: O(L) for a word of length L. Space: up to O(total letters), reduced when words share prefixes.

## Coding questions
- Q1 (Easy): Does a word exist? (dict-of-dicts trie)
- Q2 (Easy): Longest common prefix
- Q3 (Medium): Count words with a given prefix
- Q4 (Hard): Word search II (find words in a grid)

## Recap
- Tries store words by shared prefixes.
- O(L) insert/search/prefix.
- Next: graphs and BFS.

## Run
```bash
python solution.py
python -m pytest
```
