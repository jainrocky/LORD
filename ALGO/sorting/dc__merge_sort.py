import os, sys, random, warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from sorting_visualise import vis


def merge_sort(item, begin, end, visualise=None, condition=None):
    def merge(l, m, r):
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
            if condition(left[i], right[j]):
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
        if visualise:
            vis(item, 'Merge Sort', m)
            
    def sort(l, r):
        if l<r:
            m = (l+r)//2
            sort(l, m)
            sort(m+1, r)
            merge(l, m, r)
            
    if condition is None:
        condition=lambda first, second: first <= second # equality must be checked other wise un-stablity happens
    if visualise:
        warnings.warn('Visualise, required extra Modules such as numpy and matplotlib and OpenCV')
        if not isinstance(item[begin], (int, float, str)):
            raise ValueError("visualise is valid only for 'int', 'float', 'str' not for {}".format(type(item[begin])))
    sort(begin, end)
    if visualise:
            vis(item, 'Merge Sort')


if __name__=='__main__':
    n = 100
    item=[None]*n
    for i in range(n):
        item[i] = random.random()*100
    
    merge_sort(item, begin=0, end=len(item)-1, visualise=True) # non-decreasing order by first element of tuple

    more=True
    if more:
        item2 = [(314, 214),
                (2141, 4),
                (1242, 124),
                (421, 124),
                (411, 4),
                (4124, 414),
                (24124, 4),]
        print(item2)
        merge_sort(item2, begin=0, end=len(item2)-1, visualise=True, condition = lambda a, b: a[1] <= b[1])
        print(item2)


    
