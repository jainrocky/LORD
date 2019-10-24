# Graph Algorithms

- V <- Number of vertices

## Dijsktra's Algorithm

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


