import os, sys, warnings, random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from sorting_visualise import vis



def shell_sort(item, begin, end, visualise=None, condition=None, gap='std'):
    size = end-begin+1
    esc=None
    if condition is None:
        condition=lambda a, b: a<b
    if visualise:
        warnings.warn('Visualise, required extra Modules such as numpy and matplotlib and OpenCV')
        
    if gap is 'std':
        next_gap = lambda curr_gap: curr_gap>>1
        esc=next_gap(size)
    elif gap is 'hibbard':
        import math as mt
        exp = mt.ceil(mt.log2(size))
        temp=2**exp-1
        next_gap = lambda curr_gap: int((curr_gap / 2) - .5)
        esc=next_gap(temp)
    while esc > 0:
        for i in range( begin+esc, end+1 ):
            temp = item[i]
            j=i
            while j>=esc and not condition(item[j-esc], temp):
                item[j]=item[j-esc]                           
                j-=esc
            item[j]=temp
            if visualise:
                vis(item, 'Shell Sort' , j)
        esc = next_gap(esc)
    if visualise:
        vis(item, 'Shell Sort')
        

if __name__=='__main__':
    n = 20
    item=[None]*n
    for i in range(n):
        item[i] = round( random.random() * 100, 2 )
    shell_sort( item, 0, len(item)-1, gap='hibbard', visualise=True)
    print(item)
    
