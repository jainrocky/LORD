import sys, os, warnings

if __name__=='__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from adjacency_matrix import Graph

    g = Graph(5)
    g.add_edge(Graph.Edge( 0, 1, 22 ))
    g.add_edge(Graph.Edge( 1, 2, 12 ));
    g.add_edge(Graph.Edge( 2, 4, 45 ));
    g.add_edge(Graph.Edge( 4, 3, 21 ));
    g.add_edge(Graph.Edge( 3, 0, 21 ));
    g.print()
    
    points = ((10, 10),
              (10, 30),
              (20, 30),
              (20, 10),
              (30, 20))
    '''if not points then make graph with random points'''
    g.draw(points)
    
    
    
