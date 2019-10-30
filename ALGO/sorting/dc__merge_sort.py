import os, sys


def merge(item, l, m, r, cmp):
    n1 = m-l+1
    n2 = r-m
    left, right = [], []
    for i in range(l, m+1):
        left.append(item[i])
    for i in range(m+1, r+1):
        right.append(item[i])
    i, j = 0, 0
    k=l
    while i<n1 and j<n2:
        if cmp(left[i], right[j]):
            item[k] = left[i]
            i+=1
        else:
            item[k] = right[j]
            j+=1
        k+=1
    while i<n1:
        item[k] = left[i]
        i, k = i+1, k+1
    while j<n2:
        item[k]=right[j]
        j, k =j+1, k+1

def merge_sort(item, begin, end, cmp=lambda first, second: first < second):
    def sort(item, l, r):
        if l<r:
            m = (l+r)//2
            sort(item, l, m)
            sort(item, m+1, r)
            merge(item, l, m, r, cmp)
    sort(item, begin, end)

    

if __name__=='__main__':
    item = [(23, 4), (234 , 34), (34, 223), (1, 43)]
    print(*item)
    merge_sort(item, begin=0, end=len(item)-1, cmp=lambda a, b: a[0] > b[0] ) # non-decreasing order by first element of tuple
    print(*item)
