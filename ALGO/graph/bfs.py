import os, sys 
sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', '..', 'DS', 'queue' ) )
from std_queue import Queue


def bfs(l, start=0):
    n=len(l)
    visited = [False]*n
    q=Queue()
    visited[start]=True
    q.push( start )
    path = []
    while not q.empty():
        u = q.pop()
        path.append(u)
        for v, w in l[u]:
            if not visited[v]:
                q.push( v )
                visited[v]=True
    return path

if __name__=='__main__':
    sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', '..', 'DS', 'graph' ) )
    from graph import Graph
    g=Graph(n_node=4, adjacency='list')
    g.add_edge( Graph.Edge(0, 1) )
    g.add_edge( Graph.Edge(0, 2) )
    g.add_edge( Graph.Edge(1, 2) )
    g.add_edge( Graph.Edge(2, 0) )
    g.add_edge( Graph.Edge(2, 3) )
    g.add_edge( Graph.Edge(3, 3) )

    bfs_path = bfs(g.list, 2)
    print(bfs_path)

    
