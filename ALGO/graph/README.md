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

### Using Ajacency list & min heap

## Bellman-Ford Algorithm

Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph. 

Key Points:

- The graph may contain negative weight edges.
- Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of min heap). 
- Dijkstra doesn’t work for Graphs with negative weight edges
- Bellman-Ford works for such graphs.
- But time complexity of Bellman-Ford is `O(VE)`, which is more than Dijkstra.


