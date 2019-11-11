import os, sys

class BinomialHeap():
    class Node():
        def __init__(self, k):
            self.key=k
            self.par=None
            self.sib=None
            self.child=None
            self.deg=0
        def __str__(self):
            return '({}, {})'.format(self.key, self.deg)

    def __init__(self, data=None, condition=None):
        self.heap=None
        self.condition = lambda a,b: a<b
        if condition is not None:
            self.condition=condition
        if data is not None:
            for val in data:
                self.insert(val)

    def insert(self, val):
        self.merge([self.Node(k=val)])
            
    def remove(self):
        i=1
        idx=0
        removed = self.heap[idx]
        n=len(self.heap)
        while i<n:
            if self.condition(self.heap[i].key, removed.key): #if condition satisfy then stored that node
                idx=i
                removed = self.heap[idx]
            i+=1
        del self.heap[idx]
        rm_childs = []
        p = removed.child
        while p is not None:
            t=p
            p=p.sib
            t.sib=None
            t.par=None
            rm_childs.append(t)
        self.merge( rm_childs )
        return removed.key
        
    
    def exist(self):
        return len(self.heap)>0

    def insert_by_order(self, target):
        temp = []
        j=i=0
        n = len(self.heap) if self.heap else 0
        m = len(target) if target else 0
        while i<n and j<m:
            if self.heap[i].deg <= target[j].deg:
                temp.append(self.heap[i])
                i+=1
            else:
                temp.append(target[j])
                j+=1
        while i<n:
            temp.append(self.heap[i])
            i+=1
        while j<m:
            temp.append(target[j])
            j+=1
        self.heap=temp

    def merge(self, target):
        self.insert_by_order(target)
        f = 0 #pointing to 1st smallest binomial tree 
        s = 1 #pointing to 2nd smallest binomial tree 
        t = 2 #pointing to 3rd smallest binomial tree
        while f < len(self.heap):
            if s >= len(self.heap):
                break
            elif self.heap[f].deg != self.heap[s].deg:
                f, s, t = f+1, s+1, t+1
            elif t<len(self.heap) and self.heap[f].deg == self.heap[s].deg and self.heap[f].deg == self.heap[t].deg:
                f, s, t =f+1, s+1, t+1
            elif self.heap[f].deg == self.heap[s].deg:
                if not self.condition(self.heap[f].key, self.heap[s].key): # if condition voilates then swap it to make it as a child(first is always parents of second)
                    q = self.heap[f]
                    self.heap[f] = self.heap[s]
                    self.heap[s] = q
                self.heap[s].par = self.heap[f]
                self.heap[s].sib = self.heap[f].child
                self.heap[f].child = self.heap[s]
                self.heap[f].deg += 1
                del self.heap[s] #O(log(n)) <<- length of self.heap array

                    
    def print(self):
        def _print(node):
            print(node)
            if node.sib is not None:
                print('sibling of', node, end=' ')
                _print(node.sib)
            if node.child is not None:
                print('child of', node, end=' ')
                _print(node.child)
        for node in self.heap:
            _print(node)


if __name__=='__main__':
    bh = BinomialHeap(condition=lambda a, b: a>b)
    for i in range(50, 0, -1):
        bh.insert(i)
    
    while bh.exist():
        print(bh.remove(), end=' ')
    print()
    print()

    # priority example
    bh2 = BinomialHeap(data=[(12, 124),
                             (41, 121),
                             (123, 214),
                             (213, 14532),
                             (4312, 35),
                             (1, 2),
                             (21, 14),
                             (124, 12)], condition=lambda a, b: a[1] > b[1])
    
    bh2.insert((14124, 124125))
    bh2.insert((23, 532))
    bh2.insert((523, 574))
    while bh2.exist():
        print(bh2.remove(), end=' ')
    



    
