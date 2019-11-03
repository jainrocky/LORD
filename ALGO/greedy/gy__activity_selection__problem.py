import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sorting'))
from dc__quick_sort import quick_sort


def max_activity(act):
    n = len(act)
    quick_sort(act, 0, len(act)-1, condition=lambda a, b: a[1] < b[1])
    save = [act[0]]
    i=1
    while i < n:
        if save[-1][1] <= act[i][0]:
            save.append(act[i])
        i+=1
    return save
 

if __name__=='__main__':
    act = [(10, 20),
           (12, 25),
           (20, 30)]
    selected = max_activity(act)
    print(selected)

