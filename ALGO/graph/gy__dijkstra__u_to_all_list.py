import os, sys
sys.path.append(os.path.join(os.path.dirname( __file__ ), '..', '..', 'DS', 'queue'))
sys.path.append(os.path.join(os.path.dirname( __file__ ), '..', '..', 'DS', 'graph'))
from graph import Graph
from priority_queue import PriorityQueue

inf = 2**31

def least_cost_u_to_all(l, src=0):
    n = len(l)
    cost = [inf]*n
    cost[src]=0
    path = []

    pq = PriorityQueue(priority=lambda a, b: a[1] < b[1]) #MagicalQueue
    for i in range(n): # n
        pq.push( ( i, cost[i] ) ) # n + nlog(n)

    while not pq.empty():
        u, cost_u = pq.pop() 
        for v, cost_uv in l[u]:
            if cost_u !=inf and cost[v] > cost[u] + cost_uv:
                cost[v] = cost[u] + cost_uv
                pq.push( ( v, cost[v] ) ) # elog(n+e) bcz n node is already present and inserting new `e` edges
    return cost



if __name__=='__main__':
    
    g = Graph(5, adjacency='list')
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
    src_vertex=3
    c = least_cost_u_to_all(g.list, src=src_vertex)
    for i in range(len(c)):
        print('Distance from', src_vertex, 'to', i, 'is', c[i])
        



    
