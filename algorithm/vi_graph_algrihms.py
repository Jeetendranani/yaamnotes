"""
VI. Graph Algorithms

Introduction

Graph problems pervade computer science, and algorithms for working with them are fundamental to the field. Hundreds of
interesting computational problems are couched in terms of graphs. In this part, we touch on a few of the more
significant ones.

Chapter 22 shows how we can represent a graph in a computer and then discusses algorithms based on searching a graph
using either breadth-first search or depth-first search. The chapter gives two applications of depth-first search:
topologically sorting a directed acyclic graph and decomposing a directed graph into its strongly connected components.

Chapter 23 describes how to compute a minimum-weight spanning tree of a graph: the least-weight way of connecting all
of the vertices together when each edge has an associated weight. The algorithms for computing minimum spanning trees
serve as good examples of greedy algorithms (see chapter 16).

Chapter 24 and 25 consider how to compute shortest paths between vertices when each edge has an associated length or
"weight." Chapter 24 shows how to find  shortest paths from a given source vertex to all other vertices, and Chapter 25
examines methods to compute shortest paths between every pare of vertices.

Finally, Chapter 26 shows how to compute a maximum flow of material in a flow network, which is a directed graph having
a specified source vertex of material, a specified sink vertex, and specified capacities for the amount of material
that can traverse each directed edge. This general problem arise in many forms, and a good algorithm for computing
maximum flows can help solve a variety of related problems efficiently.

When we characterize the running time of a graph algorithm on a given graph G = (V, E), we usually measure the size of
the input in terms of the number of vertices |V| and the numbers of edges |E| of the graph. That is, we describe the
size of the input with two parameters, not just one. We adopt a common notational convention for these parameters.
Inside asymptotic notation (such as O-notation or O1-notation), and only inside such notation, the symbol V denotes |V|
and the E denotes |E|. For example, we might say, "the algorithm runs in time O(VE)", meaning that the algorithm runs
in time O(|V||E|). This convention makes the running-time formulas easier to read, without risk of ambiguity.

Another convention we adopt appears in pseudocode. We denote the vertex set of graph G by G. V and its edge set by G.E.
That is, the pseudocode views vertex and edge sets as attributes of a graph.
"""