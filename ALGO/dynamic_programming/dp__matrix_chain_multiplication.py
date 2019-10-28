import os, sys, warnings
inf = 2**31


def min_operation_req(m_orders, print_ord=None):
    m_count = len(m_orders)-1
    cache=[[0] * (m_count) for i in range(m_count)]
    p_cache = [[0] * (m_count) for i in range(m_count)]
    for l in range(2, m_count+1):
        for first in range(m_count-l+1):
            last = first + l-1
            cache[first][last]=inf
            for mid in range(first, last):
                temp = cache[first][mid] + cache[mid+1][last] + (m_orders[first]*m_orders[mid+1]*m_orders[last+1])
                if temp < cache[first][last]:
                    cache[first][last], p_cache[first][last] = temp, mid

    ''' Printing How matrix should be multiply to get min operations'''
    if print_ord:
        def print_order(p_cache, start, end):
            if start == end:
                print(start+1, end='')
                return
            print('( ', end='')
            print_order(p_cache, start, p_cache[start][end])
            print(' x ', end='')
            print_order(p_cache, p_cache[start][end]+1, end)
            print(' )', end='')
        print_order(p_cache, 0, m_count-1)
        print()
        
    return cache[0][-1]

    
if __name__=='__main__':
    m = [40, 20, 30, 10, 30, 43, 141, 141, 421, 24, 21, 41412, 4124, 412, 123, 43, 6645, 654, 7647]
    print('Minimun Number of opeartions:', min_operation_req(m, print_ord=True))
