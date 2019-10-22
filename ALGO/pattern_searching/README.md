# Pattern Searching

- N -> len(text)
- M -> len(pattern)

## Naive approach

* Best case `O(N)`
* Worst & Avg case `O(N*(N-M+1))` 

## Rabin karp

* Best & Avg case `O(N+M)`
* Worst case `O(N*M)` when spurious hit(hash value matches but pattern not matches) and only last character of text is not matched with a given pattern

## KMP

* Best & Avg & Worst case `O(N)`