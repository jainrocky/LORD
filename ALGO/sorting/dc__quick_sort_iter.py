import os, sys, warnings, random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'stack'))
from sorting_visualise import vis
from stack import Stack

def quick_sort(item, begin, end, visualise=None, condition=None):
            
    if condition is None:
        condition=lambda first, second: first <= second # equality must be checked other wise un-stablity happens
    if visualise:
        warnings.warn('Visualise, required extra Modules such as numpy and matplotlib and OpenCV')
        if not isinstance(item[begin], (int, float, str)):
            raise ValueError("visualise is valid only for 'int', 'float', 'str' not for {}".format(type(item[begin])))
        
    def partition(begin, end):
        pivot = end
        i=begin
        j=begin
        while i <= end-1:
            if not condition(item[pivot], item[i]):
                item[i], item[j] = item[j], item[i]
                j += 1
            i+=1
        item[j], item[pivot] = item[pivot], item[j]
        if visualise:
            vis(item, 'Quick Sort' ,pivot)
        return j
    s = Stack()
    s.push((begin, end))

    while not s.empty():# <= log(end-begin+1)
        l, h = s.pop()
        p = partition(l, h)
        if p+1<h:
            s.push(( p+1, h ))
        if l<p-1:
            s.push(( l,  p-1 ))
    if visualise:
        vis(item, 'Quick Sort')
    


if __name__=='__main__':
    n = 100
    item=[None]*n
    for i in range(n):
        item[i] = random.random()*100
    quick_sort(item, 0, len(item)-1, visualise=True, condition=lambda first, second: first > second)

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
        quick_sort(item2, begin=0, end=len(item2)-1, condition = lambda a, b: a[1] < b[1])
        print(item2)


    
