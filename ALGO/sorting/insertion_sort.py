import os, sys, random, warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from sorting_visualise import vis


def insertion_sort(item, begin, end, visualise=None, condition=None):
    if condition is None:
        condition=lambda first, second: first <= second
    if visualise:
        warnings.warn('Visualise, required extra Modules such as numpy and matplotlib and OpenCV')
        if not isinstance(item[begin], (int, float, str)):
            raise ValueError("visualise is valid only for 'int', 'float', 'str' not for {}".format(type(item[begin])))
        
    i=j=begin
    while i <= end:
        j=i
        k=item[i]
        while j > begin and not condition( item[j-1], k ):
            item[j] = item[j-1]
            j -= 1
        item[j] = k
        if visualise:
            vis(item, 'Insertion Sort', j)
        i+=1
        
    # final-sorted
    if visualise:
            vis(item, 'Insertion Sort')

    

if __name__=='__main__':
    
    n = 100
    item=[None]*n
    for i in range(n):
        item[i] = random.random()*100
    insertion_sort(item, begin=0, end=len(item)-1, visualise=True)

    more = False
    if more:
        item2 = [(314, 214),
                (2141, 4),
                (1242, 124),
                (421, 124),
                (411, 4),
                (4124, 414),
                (24124, 4),]
        print(item2)
        insertion_sort(item2, begin=0, end=len(item2)-1, condition = lambda a, b: a[1] >= b[1])
        print(item2)
