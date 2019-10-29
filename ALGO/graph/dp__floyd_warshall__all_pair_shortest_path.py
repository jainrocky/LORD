import os, sys
inf = 2**31

def all_pair_shortest_path(matrix, printing=None):
    n = len(matrix)
    p_cache = [[None] * n for i in range(n)]
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                temp = matrix[start][mid] + matrix[mid][end]
                if temp < matrix[start][end] and matrix[start][mid]!=inf and matrix[mid][end]!=inf:
                    matrix[start][end] = temp
                    p_cache[start][end] = mid
    if printing:  
        def print_path(start, end):
            print(end, end='')
            if matrix[start][end] != inf:
                print(' < ', end='')
            else:
                print(' Not Exist ', end='')
            if p_cache[start][end]:
                print_path(start, p_cache[start][end])
            if not p_cache[start][end]:
                print(start)
            
        for i in range(n):
            for j in range(n):
                print_path(i, j)
    return matrix
    

if __name__=='__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'graph'))
    from graph import Graph

    g = Graph(n_node=4)
    g.add_edge(Graph.Edge( 0, 1, 5 ))
    g.add_edge(Graph.Edge( 0, 3, 10 ))
    g.add_edge(Graph.Edge( 1, 2, 3 ))
    g.add_edge(Graph.Edge( 2, 3, 1 ))

    cost_matrix = all_pair_shortest_path(g.matrix, printing=True)
    print()
    for c in cost_matrix:
        print(*c)
        
