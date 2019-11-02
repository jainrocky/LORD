import os, sys, random

def kth_smallest(item, k):
    n = len(item)
    if k<1:
        k=1
    elif k>n:
        k=n
        
    def rand_partition(begin, end):
        z = random.randint(begin, end)
        item[z], item[end] = item[end], item[z]
        pivot = end
        i=begin
        j=begin
        while i<end:
            if item[pivot] > item[i]:
                item[i], item[j] = item[j], item[i]
                j+=1
            i+=1
        item[pivot], item[j] = item[j], item[pivot]
        return j

    def kth(begin, end, k):
        if begin==end:
            return begin
        p = rand_partition(begin, end)
        rel_p = p - begin + 1
        if rel_p==k:
            return p
        elif k < rel_p:
            return kth(begin, p-1, k)
        else:
            return kth(p+1, end, k-rel_p)
        
    return item[kth(0, n-1, k)]
            


if __name__=='__main__':
    item = [1, 124, 12, 23, 2, 43, 12, 243 ,234 ,42, 1,2 ,43 ,23, 523, 232,523, 5,23]
    print(kth_smallest(item, k=5)) # second last smallest element or 2nd largest element
    print(sorted(item))
