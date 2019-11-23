import os, sys 
sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', '..', 'DS', 'stack' ) )
from stack import Stack


def dfs(l, start=0):
    n=len(l)
    path=[]
    visited=[False]*n
    s = Stack()
    s.push( start )
    visited[start]=True
    while not s.empty():
        u = s.pop()
        path.append(u)
        for v, w in l[u]:
            if not visited[v]:
                s.push(v)
                visited[v]=True
    return path

if __name__=='__main__':
    sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', '..', 'DS', 'graph' ) )
    from graph import Graph
    
    g=Graph(n_node=5, adjacency='list')
    g.add_edge( Graph.Edge(1, 0) )
    g.add_edge( Graph.Edge(0, 2) )
    g.add_edge( Graph.Edge(2, 1) )
    g.add_edge( Graph.Edge(0, 3) )
    g.add_edge( Graph.Edge(1, 4) )
    dfs_path = dfs(g.list, )
    print(dfs_path)

    
