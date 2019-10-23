# Graph

- N -> Number of nodes

Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not same as (v, u) in case of a directed graph(di-graph). The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.

## Following two are the most commonly used representations of a graph.
* Adjacency Matrix
* Adjacency List

## Ajacency Matrix

* For creating adjacency matrix `O(N^2)`