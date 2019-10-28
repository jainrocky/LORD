import os, sys

def find_max_value(w, v, capacity):
    n = len(w)
    cache = [ [0]*(capacity+1) for i in range(n+1) ]
    p_cache = [ ['e']*(capacity+1) for i in range(n+1) ]
    for i in range(1, n+1):
        for curr_w in range(1, capacity+1):
            cache[i][curr_w] = cache[i-1][curr_w]
            p_cache[i][curr_w] = 'e'
            if curr_w >= w[i-1]:
                if cache[i-1][curr_w-w[i-1]] + v[i-1] > cache[i][curr_w]:
                    cache[i][curr_w] = cache[i-1][curr_w-w[i-1]] + v[i-1]
                    p_cache[i][curr_w] = 'i'
    i, j = n, capacity
    bag = []
    while i>0 and j>0:
        if p_cache[i][j] == 'i':
            bag.append( ( i-1, w[i-1], v[i-1] ) )
            i, j = i-1, j-w[i-1]
        else:
            i = i-1    
    return cache[n][capacity], bag

                
if __name__ == '__main__':
    w = [10, 20, 30, 342, 124, 214, 124, 6547, 54, 43, 436, 14, 14, 412, 14] # finite number of items(item can be taken only once)
    v = [60, 100, 120, 321, 131, 24, 424, 352, 2, 12341, 21, 15, 25, 15125, 3234]
    capacity = 5000
    max_value, bag = find_max_value(w, v, capacity)
    print('Max Value:', max_value)
    print('*'*10, 'Included Items', '*'*10)
    for b in bag:
        print(b)
