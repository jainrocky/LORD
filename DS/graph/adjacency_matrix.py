import sys, os, warnings

class Graph:
    class Edge:
        def __init__(self, u, v, w=1):
            self.uid, self.vid, self.weight=u, v, w        

    def __init__(self, n_node, edges=None):
        self.n_node=n_node
        self.build_matrix()
        self.edges=[]
        if edges:
            for e in edges:
                self.add_edge(e)
        
    def build_matrix(self):
        self.matrix = [[0] * self.n_node for i in range(self.n_node)]

    def add_edge(self, edge):
        if isinstance(edge, self.Edge):
            if edge.uid < self.n_node and edge.vid < self.n_node:
                self.matrix[edge.uid][edge.vid] = edge.weight
                self.edges.append(edge)
            else:
                raise SystemExit('Vertex id must be in between 0 to {}'.format(self.n_node-1))
        else:
            raise TypeError("Argument is must be of type of Edge")

    def print(self, upto=None):
        if not upto:
            upto = self.n_node
        for row in self.matrix[:upto]:
            print(*row[:upto])
    
    def draw(self, points=None, draw_n_edges=None):
        warnings.warn('draw function required extra Modules such as numpy and matplotlib')
        try:
            import matplotlib.pyplot as plt
            import numpy as np
        except:
            raise ImportError
        
        if not points:
            points = np.random.randint(0, self.n_node*10, size=(self.n_node, 2))
        if not draw_n_edges:
            draw_n_edges=len(self.edges)
            
        ax=plt.axes()
        for i, e in enumerate(self.edges[:draw_n_edges]):
            plt.plot([points[e.uid][0], points[e.vid][0]],
                    [points[e.uid][1], points[e.vid][1]])
            plt.text((points[e.uid][0]+points[e.vid][0])//2,
                     (points[e.uid][1]+points[e.vid][1])//2,
                      e.weight)
        for p in points:
            ax.add_artist( plt.Circle(p, 0.2, color=np.random.rand(3)) )
        plt.show()
    


if __name__=='__main__':
    
    with open('../../TEST_DATA/GRAPH_EDGES.txt') as f:
        for i, line in enumerate(f):
            if i==0:
                g = Graph(int(line))
            else:
                g.add_edge(edge = Graph.Edge(*map(int, line.split(' '))))
        g.print(30)
    
