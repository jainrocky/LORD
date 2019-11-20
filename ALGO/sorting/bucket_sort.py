import os, sys, random
from insertion_sort import insertion_sort

def bucket_sort(item, begin, end, key=None):
    if key is None:
        key = lambda x: x[0] if isinstance(x, (list, tuple, ) ) else x
    size    = end-begin+1
    buckets = [None]*size
    i=begin
    
    while i<=end:
        if  buckets[ int( size * key(item[i]) ) ] is None:
            buckets[ int( size * key(item[i]) ) ]=[item[i]]
        else:
            buckets[ int( size * key(item[i]) ) ].append(item[i])
        i+=1
        
    i=0
    while i<size:
        if buckets[i] is not None:
            insertion_sort(buckets[i],
                           0,
                           len(buckets[i])-1,
                           condition=lambda a, b: key(a) <= key(b)) # equality must be check for stable sorting
        i+=1

    i=0
    for bucket in buckets:
        if bucket is not None:
            for e in bucket:
                item[begin+i]=e
                i+=1


if __name__=='__main__':
    n = 20
    item=[None]*n
    for i in range(n):
        item[i] = round(random.random(), 3)
    bucket_sort(item, 0, len(item)-1) 
    print(item, end='\n'*2)

    more = True
    if more:
        item1 = [(.21, 0.112),
                 (31, .13),
                 (1, .34),
                 (12, .42),
                 (12, .13),
                 (31, .32),                 
                 (324, .13)]
        bucket_sort(item1, 0, len(item1)-1, key=lambda x: x[1]) 
        print(item1)
        
