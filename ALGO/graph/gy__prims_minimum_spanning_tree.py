import os, sys
sys.path.append(os.path.join( os.path.dirname( __file__ ), '..',  '..', 'DS', 'graph'))
sys.path.append(os.path.join( os.path.dirname( __file__ ), '..',  '..', 'DS', 'queue'))
from graph import Graph
from priority_queue import PriorityQueue

inf=2**31


def minimum_spanning_tree(l):
    n_node = len(l)
    visited=[False]*n_node
    cost=[inf]*n_node
    parent=[None]*n_node
    cost[0]=0
    parent[0]=0
    def cmp(a,b):
        if a[1]<b[1]:
            return True
        elif a[1]==b[1] and a[0]<b[0]:
            return True
        else:
            return False
    pq = PriorityQueue(priority=cmp)
    for i in range(n_node):
        pq.push( (i, cost[i]) )
        
    while not pq.empty():
        ''' Get the minimum cost element and delete that, **pq.pop()** '''
        u, u_cost = pq.pop()
        for v, uv_cost in l[u]:
            '''Check if Vertex is not considered yet, and having a minimum edge between u to v'''
            if not visited[v] and cost[v] > uv_cost:
                cost[v], parent[v] = uv_cost, u
                '''Add new updated least cost( less than the previous cost associated with the same node ), '''
                pq.push( ( v, uv_cost ) )
        visited[u] = True
    mst=[]
    '''Include only '''
    for i in range(n_node):
        if visited[i] and parent[i] is not None:
            mst.append((i, cost[i], parent[i]))
        
    return mst

if __name__=='__main__':
    points = ((10, 10),
              (10, 30),
              (30, 30),
              (30, 10),
              (20, 40))
    
    g = Graph(n_node=5, adjacency='list')
    g.add_edge( Graph.Edge( 0, 1, 2 ) )
    g.add_edge( Graph.Edge( 0, 3, 6 ) )
    g.add_edge( Graph.Edge( 1, 0, 2 ) )
##    g.add_edge( Graph.Edge( 1, 2, 3 ) )
    g.add_edge( Graph.Edge( 1, 3, 8 ) )
    g.add_edge( Graph.Edge( 1, 4, 5 ) )
    g.add_edge( Graph.Edge( 2, 1, 3 ) )
    g.add_edge( Graph.Edge( 2, 4, 7 ) )
    g.add_edge( Graph.Edge( 3, 0, 6 ) )
    g.add_edge( Graph.Edge( 3, 1, 8 ) )
    g.add_edge( Graph.Edge( 3, 4, 9 ) )
    g.add_edge( Graph.Edge( 4, 1, 5 ) )
##    g.add_edge( Graph.Edge( 4, 2, 7 ) )
    g.add_edge( Graph.Edge( 4, 3, 9 ) )

    g.draw(points)
    mst = minimum_spanning_tree(g.list)
    gnew = Graph(n_node=5)
    
    for c in mst:
        print( c[2], '___', c[0], '->', c[1])
        gnew.add_edge(Graph.Edge( c[2], c[0], c[1] ) )
    gnew.draw(points)

    
