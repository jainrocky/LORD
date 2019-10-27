import os, sys, warnings
inf=2**31

def least_cost_u_to_all(l, src=0):
    n_node = len(l)
    cost = [inf]*n_node
    parent = [None]*n_node

    cost[src]=0

    for i in range(n_node):
        for u, vset in enumerate(l):
            for v, uv_cost in vset:
                if cost[u] + uv_cost < cost[v]:
                    cost[v], parent[v] = cost[u] + uv_cost, u

    return cost, parent

if __name__=='__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'graph' ))
    from graph import Graph

    g = Graph(n_node=5, adjacency='list')

    g.add_edge( Graph.Edge( 0, 1, -1 ) )
    g.add_edge( Graph.Edge( 0, 2, 4 ) )
    g.add_edge( Graph.Edge( 1, 2, 3 ) )
    g.add_edge( Graph.Edge( 1, 3, 2 ) )
    g.add_edge( Graph.Edge( 1, 4, 2 ) )
    g.add_edge( Graph.Edge( 3, 2, 5 ) )
    g.add_edge( Graph.Edge( 3, 1, 1 ) )
    g.add_edge( Graph.Edge( 4, 3, -3 ) )

    src_vertex=3
    c, p = least_cost_u_to_all(g.list, src=src_vertex)
    
    for i in range(len(p)):
        print('Parent of vertex', i, '<-', p[i], 'and distance from', src_vertex, 'to', i, 'is', c[i])
        
    g.draw(points = ((10, 10),
              (10, 30),
              (20, 40),
              (30, 10),
              (30, 20)))    
