import os, sys, warnings, random



def counting_sort(item, begin, end):
    mn, mx = min(item[begin: end+1]), max(item[begin: end+1])
    pos = [0]*(mx-mn+1)
    
    for e in item[begin: end+1]:
        pos[e-mn]+=1
        
    for i in range(1, len(pos)):
        pos[i] += pos[i-1]
        
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
        
    i=begin
    while i<=end:
        sorted_[ begin+pos[item[i]-mn]-1 ] = item[i]
        pos[item[i]-mn] -= 1
        i+=1
    return sorted_


if __name__=='__main__':
    item = list(range(100, -30, -2))
    sort_item = counting_sort(item, 0, len(item)-1)
    print(sort_item)
