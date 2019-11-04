# Dynamic Programming

## dp__0_1_knapsack

Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack.

* Category: dp
* Worst-case: `O(n*W)`
* Average-case: `O(n*W)`
* Best-case: `O(n*W)`	

## dp__longest_common_subsequence

Given two sequences(let say x and y), find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

`n <- len(x)`
`m <- len(y)`

* Worst-case: `O(n*m)`
* Best-case: `O(n*m)`
* Average-case: `O(n*m)`
* Category: dp

## dp__matrix_chain_multiplication

- Given a sequence of matrices, find the most efficient way to multiply these matrices together.
- The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

`n <- Number of matrices`

* Category: dp
* Worst-case: `O(n^3)`
* Average-case: `O(n^3)`
* Best-case: `O(n^3)`

## dp__optimal_binary_search_tree

- Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches to keys[i]
- Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.

`n <- Number of keys`

* Category: dp
* Worst-case: `O(n^3)`
* Average-case: `O(n^3)`
* Best-case: `O(n^3)`

## dp__binomial_coefficient

To fill the table upto **nth coefficient**

* Category: dp
* Worst-case: `O(n^2)`
* Average-case: `O(n^2)`
* Best-case: `O(n^2)`

After filling table each query for each coeffiecient( < n) required
- `O(1)`


