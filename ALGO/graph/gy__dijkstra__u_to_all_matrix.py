import os, sys, warnings
inf = 2**31

'''
    By default Source vertex is zero
'''
def least_cost_u_to_all(matrix, src=0):

    def least_cost_node(visited, cost):
        least_cost, vertex = inf, None
        for u in range(len(cost)):
            if not visited[u]:
                if cost[u] <= least_cost:
                    least_cost, vertex = cost[u], u
        return vertex
    
    n_node = len(matrix)
    visited = [False]*n_node
    cost = [inf]*n_node
    parent = [None]*n_node

    ''' Cost for path from SOURCE to SOURCE is zero'''
    cost[src]=0  

    for i in range(n_node):
        u = least_cost_node(visited, cost)
        
        for v in range(0, n_node):
            if matrix[u][v] > 0 and not visited[v]:
                if ( cost[u] + matrix[u][v] ) < cost[v]:
                    cost[v], parent[v] = cost[u] + matrix[u][v], u
        visited[u]=True

    
    return cost, parent


if __name__=='__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'graph' ))
    from graph import Graph

    g = Graph(5, adjacency='matrix')
    
    g.add_edge(Graph.Edge( 0, 1, 2 ))
    g.add_edge(Graph.Edge( 0, 3, 6 ))
    g.add_edge(Graph.Edge( 1, 0, 2 ))
    g.add_edge(Graph.Edge( 1, 2, 3 ))
    g.add_edge(Graph.Edge( 1, 3, 8 ))
    g.add_edge(Graph.Edge( 1, 4, 5 ))
    g.add_edge(Graph.Edge( 2, 1, 3 ))
    g.add_edge(Graph.Edge( 2, 4 ))
    g.add_edge(Graph.Edge( 3, 0, 6 ))
    g.add_edge(Graph.Edge( 3, 1, 8 ))
    g.add_edge(Graph.Edge( 3, 4, 9 ))
    g.add_edge(Graph.Edge( 4, 1, 5 ))
    g.add_edge(Graph.Edge( 4, 2, 7 ))
    g.add_edge(Graph.Edge( 4, 3, 9 ))

    src_vertex=0
    c, p = least_cost_u_to_all(g.matrix, src=src_vertex)
    
    for i in range(len(p)):
        print('Parent of vertex', i, '<-', p[i], 'and distance from', src_vertex, 'to', i, 'is', c[i])

    if True:    
        g.draw(points = ((10, 10),
                  (10, 30),
                  (20, 30),
                  (20, 10),
                  (30, 20)))


        
