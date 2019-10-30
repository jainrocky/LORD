import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'queue'))
from priority_queue import PriorityQueue


class Node:
    def __init__(self, f, c=None, l=None, r=None):
        self.c, self.f = c, f
        self.l, self.r = l, r
    def __str__(self):
        return '({}, {})'.format(self.c, self.f)
        
def huffman_root(data):
    pq = PriorityQueue([
            Node(f=f, c=c) for c, f in data
        ],
        priority=lambda a, b: a.f < b.f)
    while pq.len > 2:
        left = pq.pop()
        right = pq.pop()
        root = Node( f=left.f + right.f, l=left, r=right )
        pq.push(root)
        
    left = pq.pop()
    right = pq.pop()
    root = Node(f=left.f + right.f, l=left, r=right )
    return root

def encode(root, code, top):
    if root.l is not None:
        code[top]=0
        encode(root.l, code, top+1)
    if root.r is not None:
        code[top]=1
        encode(root.r, code, top+1)
    if root.c is not None:
        print(root.c, '>', *code[:top])
    

if __name__=='__main__':
    data = [('a', 5),
            ('b', 9),
            ('c', 12),
            ('d', 13),
            ('e', 16),
            ('f', 45)]
    root = huffman_root(data)
    encode(root, [None]*100, 0)
    
    
