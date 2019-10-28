import os, sys, warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'tree' ))
from bst import BSTree

inf = 2**31

def obst_cost(k, f, visualise=None):
    n = len(k)
    cache = [[0]*(n+1) for i in range(n+1)]
    p_cache = [[0]*(n+1) for i in range(n+1)]

    w = [0]
    for i in range(n):
        w.append(w[i]+f[i])
        
    for i in range(n):    
        cache[i][i] = 0

    for d in range(1, n+1):
        for start in range(0, n-d+1):
            end = start+d
            cache[start][end]=inf
            for r in range(start, end):
                temp = cache[start][r] + cache[r+1][end] + w[end] - w[start]
                if temp < cache[start][end]:
                    cache[start][end] = temp
                    p_cache[start][end-1] = r
                    
    if visualise:
        tree = BSTree()
        def print_obst(l, r):
            if l <= r:
                print(k[p_cache[l][r]], f[p_cache[l][r]])
                tree.add_node(BSTree.Node( k[p_cache[l][r]] ))
                print_obst(l, p_cache[l][r]-1)
                print_obst(p_cache[l][r]+1, r)
        print_obst(0, n-1)
        tree.draw()
    
    return cache[0][n]
            
    
'''
Note: First graph window is of BST(before optimisation) close it to see after optimisation BST(or OBST)
'''

if __name__=='__main__':
    k = [10, 20, 30, 40, 50, 60, 70, 80, 90, 99]
    f = [71, 43, 321, 214, 142, 123, 124, 192, 431, 224]
    tree = BSTree()
    for n in k:
        tree.add_node(BSTree.Node( n ))
    tree.draw()
    print('Max Cost:', obst_cost(k, f, visualise=True))




