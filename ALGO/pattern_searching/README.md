# Pattern Searching

- N -> len(text)
- M -> len(pattern)

### Naive approach

* Best case `O(N)`
* Worst & Avg case `O(N*(N-M+1))` 

## rabin_karp__pattern_search

* Best-case: `O(N+M)`
* Average-case: `O(N+M)`
* Worst-case: `O(N*M)` (when spurious hit or hash value matches but pattern not matches and only last character of text is not matched with a given pattern)
* Category: ms

## finite_automata

* Worst-case: O(256 * M<sup>3</sup> + O(N)) (for building transition table and for searching)
* Category: ms

## kmp__pattern_search

- KMP algorithm preprocesses `pattern` and constructs an auxiliary `lps` of size m (same as size of pattern) which is used to skip characters while matching.
- name lps indicates longest proper prefix which is also suffix.. 

* Best-case: `O(N)`
* Average-case: `O(N)`
* Worst-case: `O(N)`
* Category: ms

