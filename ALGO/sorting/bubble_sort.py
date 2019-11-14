import os, sys, random, warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from sorting_visualise import vis

def bubble_sort(item, begin, end, visualise=None, condition=None):
    if condition is None:
        condition = lambda a, b: a<=b
    if visualise:
        warnings.warn('Visualise, required extra Modules such as numpy and matplotlib and OpenCV')
        if not isinstance(item[begin], (int, float, str)):
            raise ValueError("visualise is valid only for 'int', 'float', 'str' not for {}".format(type(item[begin])))
        
    for i in range(end-begin+1):
        for j in range(begin, end-i):
            if not condition(item[j], item[j+1]):
                item[j], item[j+1] = item[j+1], item[j]

        if visualise:
            vis(item, 'Bubble Sort', j)
    # final-sorted
    if visualise:
            vis(item, 'Bubble Sort')


if __name__=='__main__':
    n = 100
    item=[None]*n
    for i in range(n):
        item[i] = random.random()*100
    bubble_sort(item, begin=0, end=len(item)-1, visualise=True, condition=lambda a,b: a<b)

    more=False
    if more:
        item2 = [
                (314, 214),
                (2141, 4),
                (1242, 124),
                (421, 124),
                (411, 4),
                 (24, 4),
                (4124, 414),
                (24124, 4),
                ]
        print(item2)
        bubble_sort(item2, begin=0, end=len(item2)-1, condition = lambda a, b: a[1] >= b[1])
        print(item2)
