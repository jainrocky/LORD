import os, sys

def kth_smallest(item, k):
    def partition(item, begin, end, pivot_i):
        i=begin
        while i<=end:
            if item[i]==pivot_i:
                break
            i+=1
        item[end], item[i] = item[i], item[end]
        
        j=i=begin
        while i<end:
            if item[i] < item[end]:
                item[i], item[j] = item[j], item[i]
                j+=1
            i+=1
        item[j], item[end] = item[end], item[j]
        return j

    def kth(item, begin, end, k):
        if begin <= end:

            '''finding median of array item[begin: end+1] recursively'''
            size = end-begin+1
            n_grp = 0
            med=[]
            while n_grp < (size//5):
                med.append( sorted(item[begin+(n_grp*5): begin+(n_grp*5)+5])[len(item[begin+n_grp*5: begin+n_grp*5+5])//2] )
                n_grp += 1
            if n_grp * 5 < size:
                med.append( sorted(item[begin+n_grp*5: begin+n_grp*5 + size%5])[len(item[begin+n_grp*5: begin+n_grp*5 + size%5])//2] )
                n_grp += 1
            med_med_i = med[0] if n_grp==1 else kth( med, 0, n_grp-1, (n_grp)//2 )

            '''finding the kth rank element recursively'''
            q = partition(item, begin, end, med_med_i)
            rel_q = q-begin+1
            if rel_q == k:
                return item[q]
            elif k < rel_q:
                return kth(item, begin, q-1, k)
            else:
                return kth(item, q+1, end, k-rel_q)
    return kth(item, 0, len(item)-1, k)


if __name__=='__main__':
    item = [12, 4, 1 ,342, 23, 235, 264, 2352, 124]
    k=2
    print('length: ', len(item))
    print(str(k)+' Smallest element:', kth_smallest(item, k))
    print(sorted(item))
