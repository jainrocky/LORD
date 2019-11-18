import os, sys, warnings, random



def counting_sort(item, begin, end, key=None):
    if key is None:
        key = lambda x: x[0] if isinstance(x, (list, tuple)) else x
    mn, mx = sys.maxsize, -sys.maxsize
    i=begin
    '''finding min and max element'''
    while i+1 <= end:
        if key(item[i]) < key(item[i+1]):
            mn = key(item[i]) if key(item[i]) < mn else mn
            mx = key(item[i+1]) if key(item[i+1]) > mx else mx
        else:
            mn = key(item[i+1]) if key(item[i+1]) < mn else mn
            mx = key(item[i]) if key(item[i]) > mx else mx
        i+=2
        
    if key(item[end]) < mn:
        mn = key(item[end])
    if key(item[end]) > mx:
        mx=key(item[end])
            
    pos = [0]*(mx-mn+1)
    n=len(item)
    sorted_ = [None]*n
    i=0
    while i<begin:
        sorted_[i]=item[i]
        i+=1
    i=end+1
    
    while i<n:
        sorted_[i]=item[i]
        i+=1
        
    for e in item[begin: end+1]:
        pos[key(e)-mn]+=1
        
    for i in range(1, len(pos)):
        pos[i] += pos[i-1]
        
    i=end
    while i>=begin:
        sorted_[ begin+pos[key(item[i])-mn]-1 ] = item[i]
        pos[key(item[i])-mn] -= 1
        i-=1
    return sorted_


if __name__=='__main__':
    item = list(range(100, -30, -2))
    sort_item = counting_sort(item, 0, len(item)-1)
    print(sort_item, end='\n'*2)

    more=True
    if more:
        item1=[(21, 14),
               (31, 132),
               (131, 12),
               (1231, 1),
               (131, 13)]
        sort2=counting_sort(item1, 0, len(item1)-1, key=lambda x: x[0])
        print(sort2)
    
