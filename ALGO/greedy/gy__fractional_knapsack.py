import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sorting'))
from dc__merge_sort import merge_sort

def find_max_value(w, v, capacity):
    n = len(w)
    item = []
    for i in range(n):
        item.append( ( w[i], v[i], i ) )
    merge_sort( item, 0, n-1, cmp = lambda a, b : (a[1] / a[0]) > (b[1] / b[0]) )
    bag=[]
    val, wt=0, 0
    for i in range(n):
        if ( wt + item[i][0] ) <= capacity:
            val += item[i][1]
            wt += item[i][0]
            bag.append((item[i][2], item[i][0], item[i][1], '100%'))
        else:
            val += ( item[i][1] / item[i][0] ) * ( capacity - wt )
            bag.append((item[i][2], item[i][0], item[i][1], '{:.2f}%'.format((capacity-wt)*100/item[i][0])))
            break
    return val, bag

                
if __name__ == '__main__':
    w = [10, 20, 30, 342, 124, 214, 124, 6547, 54, 43, 436, 14, 14, 412, 14] # finite number of items(item can be taken only once)
    v = [60, 100, 120, 321, 131, 24, 424, 352, 2, 12341, 21, 15, 25, 15125, 3234]
    capacity = 5000
    max_value, bag = find_max_value(w, v, capacity)
    print('Max Value:', max_value)
    print('*'*10, 'Included Items', '*'*10)
    for b in bag:
        print(b)
