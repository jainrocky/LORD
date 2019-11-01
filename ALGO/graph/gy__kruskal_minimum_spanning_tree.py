import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'DS', 'graph'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from graph import Graph
from sorting.dc__merge_sort import merge_sort


def minimum_spanning_tree(edges, n_node):
    n_edges = len(edges)
    merge_sort(edges, begin=0, end=len(edges)-1, cmp=lambda a, b: a.weight < b.weight)
    
    '''cache_union is used to perform find_union operation on disjoint sets'''
    cache_union = [-1] * n_node # all vertices are parents intially
    mst=[]
    i=0
    while len(mst) < n_node-1 and i<n_edges: # while edges not equal to required for mst i.e, (V-1)
        e =edges[i]
        i+=1
        u, v = e.uid, e.vid
        par_u, par_v = cache_union[u], cache_union[v]
        if par_u > 0: # CHECK if it is a child
            while cache_union[par_u] > 0:
                par_u = cache_union[par_u]
                cache_union[u] = par_u #to avoid collapsing, direct assign to parent node
        else: # if not a child, then take it as a parent of itself
            par_u = u
            
        if par_v > 0: # same as above for destination Vertex
            while cache_union[par_v] > 0:
                par_v = cache_union[par_v]
                cache_union[v] = par_v
        else:
            par_v = v

        ''' if parent of both the vertex is different(or they belongs to different sets)
            then take union of them, make most negative one(or having greater number of nodes attached)
            as a parent and another one as a child of it.
        '''
        if par_u != par_v:
            mst.append(e)
            if cache_union[par_u] < cache_union[par_v]:
                cache_union[par_u] += cache_union[par_v]
                cache_union[par_v] = par_u
            else:
                cache_union[par_v] += cache_union[par_u]
                cache_union[par_u] = par_v
    return mst


if __name__=='__main__':
    
    n_node=9
    g = Graph( n_node )
    g.add_edge( Graph.Edge( 0, 1, 4 ) )
    g.add_edge( Graph.Edge( 1, 2, 8 ) )
    g.add_edge( Graph.Edge( 2, 3, 7 ) )
    g.add_edge( Graph.Edge( 3, 4, 9 ) )
    g.add_edge( Graph.Edge( 4, 5, 10 ))
    g.add_edge( Graph.Edge( 5, 6, 2 ) )
    g.add_edge( Graph.Edge( 6, 7, 10 ) )
    g.add_edge( Graph.Edge( 7, 8, 7 ) )
    g.add_edge( Graph.Edge( 0, 7, 8 ) )
    g.add_edge( Graph.Edge( 1, 7, 11) )
    g.add_edge( Graph.Edge( 2, 8, 2 ) )
    g.add_edge( Graph.Edge( 8, 6, 6 ) )
    g.add_edge( Graph.Edge( 2, 5, 4 ) )
    g.add_edge( Graph.Edge( 3, 5, 14 ) )
    
    mst = minimum_spanning_tree(g.edges, n_node)
    
    gnew = Graph(n_node)
    for e in mst:
        gnew.add_edge(e)

    points=[(10, 20),(30, 30),(50, 30),
            (80, 30),(90, 20),(80, 10),
            (50, 10),(30, 10),(50, 20)]
    g.draw(title='Graph(or Before)', points=points)
    gnew.draw(title='MST(or after)', points=points)


    
    
