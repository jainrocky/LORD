# Tree

## BSTree

### Example Image

![EXAMPLE](./img/bst_example.PNG)


## BinaryHeapTree

		 _________________________1________________________     	          -------------> level-0 / root
		|						   |	
	 _______2______________				 __________3_________     	  -------------> level-1 / third-last / 
        |    	               |                        |      		     |   
 _______4_______	 ______5________	 _______6________	 ____8_____	  -------------> level-2 / second-last / internal-node (8 is the last internal node)
|	        |       |     	        |       |       	 |      |          |
9  		10 	11		12 	13		14 	15 	   16     -------------> level-3 / last-level / leaf-nodes


`n <- Number of node in tree`

- For heapify using sift down, start from last internal node(or second last level's last node) and
- compare it with there both the childs
- if heap condition is violate then swap(for max heap swap with largest child and for min heap swap with smallest child) them
- now do the same steps for all there siblings(all others node of second last level)
- then move to third-last level and compare it with there both left and right child, if heap property violate then swap them
- now further check it with there left.left, left.left.left and so on childs till it not reach to the leaf node and do same for right.right...
- now with all there siblings and continue this process untill you reach to the level-0

- build-time `O(n)`
- insert `O(log(n))` and `O(n)` if resize
- remove `O(log(n))`