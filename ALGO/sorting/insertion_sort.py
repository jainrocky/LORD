import os, sys


def insertion_sort(item, begin, end, condition=None):
    if condition is None:
        condition=lambda first, second: first < second
    n = len(item)
    i=0
    j=0
    while i < n:
        j=i
        k=item[i]
        while j > 0 and not condition( item[j-1], k ):
            item[j] = item[j-1]
            j -= 1
        item[j] = k
        i+=1
    

if __name__=='__main__':
    item = [4, 3, 2, 10, 12, 1, 5, 6, 3, 1, 41, 124, 12, 1, 536, 36]
    insertion_sort(item, begin=0, end=len(item)-1)
    print(item)
