import os, sys, warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tree'))
from binary_heap import BinaryHeap

class PriorityQueue(BinaryHeap):
    def __init__(self, data=None, priority=None):
        super().__init__(data=data, cmp=priority)
    def push(self, val):
        self.insert(val)
    def pop(self):
        return self.remove()
    def front(self):
        return self.root()
    def empty(self):
        return self.exist() == 0
    
   
if __name__=='__main__':
    data = [1, 2, 112, 4125, 253, 67, 23, 9, 29, 68, 457]
    pq = PriorityQueue(data=data, priority=lambda first, second: first > second)
    pq.push(21324)
    pq.push(-123)
    pq.push(-13)
    pq.push(-90)
    
    while not pq.empty():
        print(pq.pop())
    
