# Dynamic Programming

## 0_1 knapsack

Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack.

- Wosrt/Avg/Best -case: `O(n*W)`

## Longest common subsequence

Given two sequences(let say x and y), find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

`n <- len(x)`
`m <- len(y)`

- Wosrt/Avg/Best -case: `O(n*m)`

## Matrix chain multiplication

- Given a sequence of matrices, find the most efficient way to multiply these matrices together.
- The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

`n <- Number of matrices`
- Wosrt/Avg/Best -case: `O(n^3)`

## Optimal binary search tree

- Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches to keys[i]
- Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.

`n <- Number of keys`
- Wosrt/Avg/Best -case: `O(n^3)`

## Binomial coefficient 

To fill the table upto **nth coefficient**
- `O(n*n)`

After filling table each query for each coeffiecient( < n) required
- `O(1)`


