# Sorting Algorithms

- `n <- len(array)`

## dc__merge_sort

* [ ] in-place
* [x] stable (used equal operator with less or greater operator when comparing otherwise it tends to un-stable)
* Worst-case: `O(nlog(n))`
* Average-case: `O(nlog(n))`
* Best-case: `O(nlog(n))`
* Category: dc

## dc__quick_sort

* [x] in-place
* [ ] stable (un-stable, even if we check for equality)
* Best-case: `O(nlog(n))`
* Average-case: `O(nlog(n))`
* Worst-case: `O(n^2)` when already sorted with opposite `condition`
* Category: dc

## dc__quick_sort_iter

* no recursion depth problem
* [x] in-place
* [ ] stable (un-stable, even if we check for equality)
* Best-case: `O(nlog(n))`
* Average-case: `O(nlog(n))`
* Worst-case: `O(n^2)` when already sorted with opposite `condition`
* Category: dc


## insertion_sort

* [x] in-place
* [x] stable (equality must be checked)
* Best-case: `O(n)`
* Average-case: `O(n^2)`
* Worst-case: `O(n^2)`
* Category: ms

## selection_sort

(for non-decreasing)
In selection sort, start from index 0 intial say it's index(i.e 0) as smallest element index store this index
now search for the next(i.e, array[0] <= array[next])smallest element from 1 to n-1 replace this smallest element index to which we prev. stored
now after travelling to till the end(i.e, here n-1) replace the `0` element with smallest element(we know there index)
now repeat this process for index `1` then for index `2` and so on till the n-2

* [x] in-place
* [ ] stable (un-stable, even if we check for equality)
* Best-case: `O(n^2)`
* Average-case: `O(n^2)`
* Worst-case: `O(n^2)`

## bubble_sort

* [x] in-place
* [x] stable (equality must be checked) 	
* Best-case: `O(n^2)`
* Average-case: `O(n^2)`
* Worst-case: `O(n^2)`
