# Graph Algorithms

- V <- Number of Vertices
- E <- Number of Edges

## gy__dijkstra__u_to_all_matrix

Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.

Key Points:
- Updation of vertex cost(for e.g. INF to `c`) is called as Relaxation.
`	if(d[u] + c(u, v) < d[v]):
		d[v] = d[u] + c(u, v)
`

- Not Applicable for negative cost edges

* Worst-case: `O(n^2)`
* Category: gy

## gy__dijkstra__u_to_all_list

* Worst-case: `O((E+V)log(V))`
* Category: gy

## dp__bellman_ford__u_to_all_list

Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph. 

Key Points:

- The graph may contain negative weight edges.
- Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of min heap). 
- work for Graphs with negative weight edges, But doesn't work with negative cycles
- But time complexity of Bellman-Ford is `O(VE)`, which is more than Dijkstra.

* Category: dp
* Worst-case: `O(VE)`

## dp__floyd_warshall__all_pair_shortest_path

- The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.
- work with negative edges, but doesn't work with negative cycles

* Worst-case `O(V^3)`
* Category: dp

## gy__prims_minimum_spanning_tree

- Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. 
- A single graph can have many different spanning trees.

* Worst-case: `O((E+V)log(V))`
* Category: gy

## gy__kruskal_minimum_spanning_tree

* Worst-case: `O(Elog(E))`
* Category: gy