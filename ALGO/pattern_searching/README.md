# Pattern Searching

- N -> len(text)
- M -> len(pattern)

## Naive approach

* Best case `O(N)`
* Worst & Avg case `O(N*(N-M+1))` 

## Rabin karp

* Best & Avg case `O(N+M)`
* Worst case `O(N*M)` when spurious hit(hash value matches but pattern not matches) and only last character of text is not matched with a given pattern

## finite_automata

* Best & Avg & Worst `O(N)` (for searching)
* O(256 * M<sup>3</sup>) (for building transition table)

## KMP

- KMP algorithm preprocesses `pattern` and constructs an auxiliary `lps` of size m (same as size of pattern) which is used to skip characters while matching.
- name lps indicates longest proper prefix which is also suffix.. 

* Best & Avg & Worst case `O(N)`

