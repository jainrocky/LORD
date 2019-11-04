# LORD

## Content

### Divide & Conquer

Name | Best-case | Average-case | Worst-case | Misc
-- | -- | -- | -- | --
[dc__randomized_select__kth_smallest_or_largest](ALGO/divide_and_conquer/dc__randomized_select__kth_smallest_or_largest.py) | `O(n)` | `O(n)` | `O(n^2)` | 
[dc__merge_sort](ALGO/sorting/dc__merge_sort.py) | `O(nlog(n))` | `O(nlog(n))` | `O(nlog(n))` | 
[dc__quick_sort](ALGO/sorting/dc__quick_sort.py) | `O(nlog(n))` | `O(nlog(n))` | `O(n^2)` when already sorted with opposite `condition` | 

### Dynamic Programming

Name | Best-case | Average-case | Worst-case | Misc
-- | -- | -- | -- | --
[dp__0_1_knapsack](ALGO/dynamic_programming/dp__0_1_knapsack.py) | `O(n*W)` | `O(n*W)` | `O(n*W)` | 
[dp__longest_common_subsequence](ALGO/dynamic_programming/dp__longest_common_subsequence.py) | `O(n*m)` | `O(n*m)` | `O(n*m)` | 
[dp__matrix_chain_multiplication](ALGO/dynamic_programming/dp__matrix_chain_multiplication.py) | `O(n^3)` | `O(n^3)` | `O(n^3)` | 
[dp__optimal_binary_search_tree](ALGO/dynamic_programming/dp__optimal_binary_search_tree.py) | `O(n^3)` | `O(n^3)` | `O(n^3)` | 
[dp__binomial_coefficient](ALGO/dynamic_programming/dp__binomial_coefficient.py) | `O(n^2)` | `O(n^2)` | `O(n^2)` | 
[dp__bellman_ford__u_to_all_list](ALGO/graph/dp__bellman_ford__u_to_all_list.py) |  |  | `O(VE)` | 
[dp__floyd_warshall__all_pair_shortest_path](ALGO/graph/dp__floyd_warshall__all_pair_shortest_path.py) |  |  |  | 

### Greedy Algorithms

Name | Best-case | Average-case | Worst-case | Misc
-- | -- | -- | -- | --
[gy__dijkstra__u_to_all_matrix](ALGO/graph/gy__dijkstra__u_to_all_matrix.py) |  |  | `O(n^2)` | 
[gy__dijkstra__u_to_all_list](ALGO/graph/gy__dijkstra__u_to_all_list.py) |  |  | `O((E+V)log(V))` | 
[gy__prims_minimum_spanning_tree](ALGO/graph/gy__prims_minimum_spanning_tree.py) |  |  | `O((E+V)log(V))` | 
[gy__kruskal_minimum_spanning_tree](ALGO/graph/gy__kruskal_minimum_spanning_tree.py) |  |  | `O(Elog(E))` | 
[gy__fractional_knapsack](ALGO/greedy/gy__fractional_knapsack.py) |  |  | `O(nlog(n))` | 
[gy__huffman_encoding](ALGO/greedy/gy__huffman_encoding.py) |  |  | O(nlog(n)) (For **pop** elements n times) | 
[gy__activity_selection__problem](ALGO/greedy/gy__activity_selection__problem.py) |  |  | `O(nlog(n))` Time for sorting(quick_sort) | 
[gy__task_scheduling__problem](ALGO/greedy/gy__task_scheduling__problem.py) |  |  | `O(nlog(n))` Time for sorting(quick_sort) | 

### Miscellaneous

Name | Best-case | Average-case | Worst-case | Misc
-- | -- | -- | -- | --
[rabin_karp__pattern_search](ALGO/pattern_searching/rabin_karp__pattern_search.py) | `O(N+M)` | `O(N+M)` | `O(N*M)` (when spurious hit or hash value matches but pattern not matches and only last character of text is not matched with a given pattern) | 
[finite_automata](ALGO/pattern_searching/finite_automata.py) |  |  | O(256 * M<sup>3</sup> + O(N)) (for building transition table and for searching) | 
[kmp__pattern_search](ALGO/pattern_searching/kmp__pattern_search.py) | `O(N)` | `O(N)` | `O(N)` | 
[insertion_sort](ALGO/sorting/insertion_sort.py) | `O(n)` | `O(n^2)` | `O(n^2)` | 