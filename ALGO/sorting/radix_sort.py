import os, sys

def radix_sort(item, begin, end, key=None):
    n = end-begin+1
    if key is None:
        key=lambda x: x[0] if isinstance(x, (list, tuple, )) else x
        
    def counting_sort(exp):
        pos = [0]*10
        sorted_=[None]*n
        for e in item[begin: end+1]:
            pos[ (key(e)//exp)%10  ] += 1
        for i in range(1, 10):
            pos[i]+=pos[i-1]
        for i in range(end, begin-1, -1):
            sorted_[ pos[ (key(item[i])//exp)%10 ]-1] = item[i]
            pos[ (key(item[i])//exp)%10 ]-=1
        return sorted_
    exp=1
    mx = key( max(item[begin: end+1], key=key) )
    while (mx // exp) > 0:
        temp = counting_sort(exp)
        for i, e in enumerate(temp):
            item[ begin + i ] = e
        exp*=10
        

if __name__=='__main__':
    item = list(range(100, 0, -3))
    radix_sort(item, 0, len(item)-1)
    print(item, end='\n'*2)

    more=True
    if more:
        item1 = [(13, 12),
                 (12 ,312),
                 (13, 123),
                 (123, 1),
                 (23 ,32),
                 (42, 43),
                 (234, 43)]
        radix_sort(item1, 0, len(item1)-1, key=lambda x : x[1])
        print(item1)
    
