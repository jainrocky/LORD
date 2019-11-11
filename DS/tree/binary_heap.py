import os, sys, warnings
import math as mt

class BinaryHeap:
    def __init__(self, data=None, cmp=None ):
        if cmp is not None:
            self.cmp=cmp
        else:
            self.cmp=lambda a, b: a>b
        if data:
            self.capacity = len(data)
            self.len = len(data)
            self.tree = data.copy()
            self.build()
        else:
            self.capacity = 5
            self.len = 0
            self.tree = [None] * self.capacity
            
    def build(self):
        last_i = 2**(mt.ceil(mt.log2(self.len))-1)-2 # last internal node (e.g: for n=15, internal node is 7th)

        #sift-down_heapify | TimeComplexity: ~O(n)
        for parent_i in range(last_i, -1, -1): # heapify last_ith to 0th node
            self.heapify_down(parent_i)

    def insert(self, val):
        if self.capacity <= self.len:
            self.resize()            
        self.tree[self.len] = val
        child_i=self.len
        parent_i  = self.parent(child_i)
        self.len += 1
        
        #shift-up
        while child_i > 0 and not self.cmp(self.tree[parent_i] , self.tree[child_i]): # Custom or default Compare function
            self.tree[parent_i], self.tree[child_i],  = self.tree[child_i],  self.tree[parent_i]
            child_i  = parent_i
            parent_i = self.parent(child_i)
                 
    def remove(self):
        removed=None
        if self.len > 0:
            removed = self.tree[0]
            self.len -= 1
            self.tree[0] = self.tree[self.len]
            self.tree[self.len]=None
        if self.len > 0:
            self.heapify_down(0)
        return removed

    def heapify_down(self, parent_i):
        left_i  = self.left(parent_i)
        right_i = self.right(parent_i)
        temp_i=None
        while left_i < self.len or  right_i < self.len :
            temp_i = left_i if left_i < self.len   and not self.cmp(self.tree[parent_i], self.tree[left_i]) else parent_i # Custom or default Compare function
            temp_i = right_i if right_i < self.len and not self.cmp(self.tree[temp_i],  self.tree[right_i]) else temp_i # Custom or default Compare function
            if temp_i is not parent_i:
                self.tree[temp_i], self.tree[parent_i] = self.tree[parent_i], self.tree[temp_i]
            else:
                break
            parent_i = temp_i
            left_i = self.left(parent_i)
            right_i = self.right(parent_i)
            
    def resize(self):
        self.capacity <<= 1
        temp = [None]*self.capacity
        for i in range(self.len):
            temp[i]=self.tree[i]
        self.tree  = temp
    def root(self):
        return self.tree[0] if self.len>0 else None
    def exist(self):
        return self.len > 0
    def left(self, i):
        return (i<<1)+1
    def right(self, i):
        return (i<<1)+2
    def parent(self, i):
        return (i-1)>>1
        
if __name__=='__main__':
    
    tree = BinaryHeap(cmp=lambda parent, child: parent > child) # Build heap based on **cmp** function condition 
    tree.insert(23)
    tree.insert(4)
    tree.insert(42)
    tree.insert(21)
    tree.insert(235)
    tree.insert(2352)
    tree.insert(2131)
    tree.insert(242)
    tree.insert(10)
    tree.insert(49)
    tree.insert(42)
    tree.insert(324)
    tree.insert(11232)
    tree.insert(21)
    tree.insert(22342)
    while tree.exist():
        print(tree.remove())

    
    more = True
    if more:
        print('\n', '*'*20, 'More Use Cases', '*'*20)
        print('Example-1\n')
        
        data = [(12, 24),
                (124, 12),
                (123, 12),
                (213, 4214),
                (24, 654),]
        ex1 = BinaryHeap(data=data, cmp=lambda a, b: a[1] < b[1])
        while ex1.exist():
            print(ex1.remove())

        print('\nExample-2\n')
        
        data = ['a', 'v', 'd', 'm', 'r', 'c', 'p', 'u', 'e', 'q', 's']
        ex2 = BinaryHeap(data=data)
        ex2.insert(val='z')
        ex2.insert(val='b')
        ex2.insert(val='y')
        ex2.insert(val='o')
        ex2.insert(val='n')
        
        while ex2.exist():
            print(ex2.remove())




    
    
    

        
