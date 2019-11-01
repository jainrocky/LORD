# Graph Algorithms

- V <- Number of Vertices
- E <- Number of Edges

## Dijkstra's Algorithm

Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.

Key Points:
- Updation of vertex cost(for e.g. INF to `c`) is called as Relaxation.
`	if(d[u] + c(u, v) < d[v]):
		d[v] = d[u] + c(u, v)
`

- Not Applicable for negative cost edges

### Using Adjacency matrix

- `O(V^2)`

### Using Ajacency list & PriorityQueue(BinaryMinHeap)

- `O((E+V)log(V))`

## Bellman-Ford Algorithm

Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph. 

Key Points:

- The graph may contain negative weight edges.
- Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of min heap). 
- work for Graphs with negative weight edges, But doesn't work with negative cycles
- But time complexity of Bellman-Ford is `O(VE)`, which is more than Dijkstra.

## Floyd Warshall Algorithm

- The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.
- work with negative edges, but doesn't work with negative cycles

- `O(V^3)`

## Prims Minimum spanning tree

- Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. 
- A single graph can have many different spanning trees.

- `O((E+V)log(V))`

## Kruskal Minimum spanning tree

- `O(Elog(E))`