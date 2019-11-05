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

    def median_of_medians(medians, begin, end, k):
        if begin <= end:
            size = end-begin+1
            med=[]
            i=0
            while i<(size//5):
                med.append( sorted( medians[ begin+i*5: begin+i*5+5 ] )[len(medians[begin+i*5: begin+i*5+5])//2] )
                i+=1
            if i*5 < size:
                med.append( sorted(medians[begin+i*5: begin+i*5 + size%5])[len(medians[begin+i*5: begin+i*5 + size%5])//2] )
                i+=1
            med_med =  med[0] if i==1 else median_of_medians( med, 0, i-1, i//2 )
            q = partition( medians, begin, end, med_med )
            l = q-begin+1
            if k == l:
                return medians[q]
            elif k < l:
                return median_of_medians( medians, begin, q-1, k )
            else:
                return median_of_medians( medians, q+1, end, k-l )

    def kth(item, begin, end, k):
        if begin<=end:
            med_med = median_of_medians(item, begin, end, k)
            q = partition(item, begin, end, med_med)
            l=q-begin+1
            if l == k:
                return item[q]
            elif k < l:
                return kth(item, begin, q-1, k)
            else:
                return kth(item, q+1, end, k-l)
    return kth(item, 0, len(item)-1, k)

    

if __name__=='__main__':
    item = [12, 4, 1 ,342, 23, 235, 264, 2352, 124]
    k=6
    print('length: ', len(item))
    print(str(k)+' Smallest element:', kth_smallest(item, k))
    print(sorted(item))
