import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sorting'))
from dc__quick_sort import quick_sort
inf = 2**31

def min_penalty(task_set):
    n = len(task_set)
    quick_sort(task_set, 0, end=n-1, condition=lambda a, b : a[2] > b[2])
    max_time = -inf
    for i in range(n):
        if task_set[i][1] > max_time:
            max_time = task_set[i][1]
    slot_set = [i for i in range(max_time+1)]
    save=[]
    i=0
    
    def find_slot(max_slot):
        while max_slot > 0 and slot_set[max_slot] != max_slot:
            max_slot = slot_set[max_slot]
        return max_slot
    
    while i < n:
        slot = find_slot(task_set[i][1])
        if slot > 0:
            save.append(task_set[i])
            next_slot = find_slot(slot-1)
            slot_set[slot] = next_slot
            slot_set[task_set[i][1]] = next_slot #optimisation, send directly to avail node if hit another time
        i+=1    
    return save # array of completed task

if __name__=='__main__':
    task_set1 = [(1, 3, 100),
                 (2, 3, 300),
                 (3, 3, 10),
                 (4, 1, 5),]
    
    penalty = min_penalty(task_set1)
    for p in penalty:
        print(p)
