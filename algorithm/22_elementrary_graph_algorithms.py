"""
Elementary Graph Algorithms

This chapter presents methods for representing a graph and for searching a graph. Searching a graph means systematically
following the edges of the graph so as to visit the vertices of the graph. A graph-searching algorithms can discover
much about the structure of a graph. many algorithms begin by searching their input graph to obtains this structural
information. Several other graph algorithms elaborate on basic graph searching. Techniques for searching a graph lie at
the heart of the field of graph algorithms.

Section 22.1 discusses the two most common computational representations of graphs: as adjacency lists and as adjacency
matrices. Section 22.2 presents a simple graph-searching algorithm called breadth-first search and shows how to create
a breadth-first tree. Section 22.3 presents depth-first search and proves some standard results about the order in
which depth-first search and proves some standard result about the order in which depth-first search and proves some
standard result about the order in which depth-first search visits vertices. Section 22.4 provides our first real
application of depth-first search: topologically sorting a directed acyclic graph. A second application of depth-first
search, finding the strongly connected components of a directed graph, it the topic of section 22.5.

22.1 Representations of graphs

We can choose between two standard ways to represent a graph G = (V, E): as a collection of adjacency lists or as an
adjacency matrix. Either way applies to both directed and undirected graphs. because the adjacency-list representation
provides a compact way to represent sparse graphs - those for which |E| is much less than |V|**2 - it is usually the
method of choice. Most of the graph algorithms presented in this book assume that an input graphs is represented in
adjacency list from. We may prefer an adjacency-matrix representation. however, when the graph is dense - |E| is close
|V|**2 or when we need to be able to tell quickly if there is an edge connecting two given vertices. For example, two
of the all-pairs shortest-paths algorithms presented in chapter 25 assume that their input graphs are represented by
adjacency matrices.

The adjacency-list representation of a graph G = (V, E) consists of an array adj of |V| lists, one for each vertex in V.
For each u < V, the adjacency list adj[v] contains all the vertices v such that there is an edge (u, v) < E. That is
adj[u] consists of all the vertices adjacent to u in G. (Alternatively, it may contains pointers to these vertices.)
Since the adjacency lists represent the edges of a graph, in pseudocode we treat the array adj as an attribute of the
graph, just as we treat the edge set E. In pseudocode therefore, we will see notation such as G. adj[u]. Figure 22.1(b)
is an adjacency-list representation of the undirected graph in Figure 22.1(a). Similarly, Figure 22.2(b) is an
adjacency list representation of the directed graph in Figure 22.2(a)

If G is a directed graph, the sum of the lengths of all the adjacency list is |E|, since an edge of the form (u, v) is
represented by having v appear in adj[u]. If G is an undirected graph, the sum of the lengths of all the adjacency lists
is 2|E|, since (u, v) is an undirected edge, then u appears in v's adjacency list and vice versa. For both directed and
undirected graphs, the adjacency-list representation has the desirable property that the amount of memory it requires is
O(V + E).

We can readily adapt adjacency lists to represent weighted graphs, that is , graphs for which each edge has an
associated weight, typically given by a weight function w: E -> R. For example, let G = (V, E) be a weighted graph with
function w. We simply store the weight w(u, v) of the edge (u, v) < E with vertex v in u's adjacency list. The
adjacency-list representation is quite robust in that we can modify it to support many other graph variants.

A potential disadvantage of the adjacency-list representation is that it provides no quicker way to determine whether a
given edge (u, v) is present in the graph than to search for v in the adjacency list adj[u]. An adjacency-matrix
representation of the graph remedies this disadvantage, but at the cost of using asymptotically more memory.

For the adjacency-matrix representation of a graph G = (V, E), we assume that the vertices are numbered 1, 2, ... |V| in
some arbitrary manner. Then the adjacency-matrix representation of a graph G consists of a |V| x |V| matrix A = (aij)
such that. Figure 22.1(c) and 22.2(c) are the adjacency matrices of the undirected and directed graphs in Figures 22.1
(a) and 22.2(a), respectively. The adjacency matrix of a graph requires O1(V**2) memory, independent of the number of
edges in the graph.

Observe the symmetry along the main diagonal of the adjacency matrix in Figure 22.1(c). Since in an undirected graph,
(U, v) and (v, u) represent the same edge, the adjacency matrix A of an undirected graph is tis own transpose: A =
A ** T. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix,
thereby cutting the memory needed to store the graph almost in half.

Like the adjacency-list representation of a graph, an adjacency matrix can represent a weighted graph. For example, if
G = (V, E) is a weighted graph with edge weight function w, we can simply store the weight w(u, v) of the edge (u, v)
< E as th entry in row u and column v of teh adjacency matrix. If an edge does not exist, we can store an Nil value as
its corresponding matrix entry, though for many leetcode it is convenient to use a value such as 0 or inf.

Although the adjacency-list representation is asymptotically at least as space-efficient as the adjacency-matrix
representation, adjacency matrices are simpler, and so we may prefer them when graphs are reasonably small. Moreover,
adjacency matrices carry a further advantage for unweighted graphs: they requires only one bit per entry.

Representing attributes

Most algorithms that operate on graphs need to maintain attributes for vertices and / or edges. We indicate these
attributes using our usual notation, such as v.d for a attribute d of a vertex v. When we indicate edges as pairs of
vertices, we use the same style of notation. For example, if edges have an attribute f, then we denote this attribute
for edge (u, v) by (u, v).f. for the purpose of presenting and understanding algorithms, our attribute notation
suffices.

Implementing vertex and edge attributes in real programs can be another story entirely. There is no one best way to
store and access vertex and edge attributes. For a given situation, you decision well likely depend on the programming
language you are using, the algorithm you are implementing, and how the rest of your program uses the graph. If you
represent a graph using adjacency lists, one design represents vertex attributes in additional arrays, such as an
array d[1 .. |V|] that parallels the adj array. If the vertices adjacent to u are in Adj[u], then what we call the
attribute u.d would actually be stored in the array entry d[u]. Many other ways of implementing attributes are possible.
For example, in an object-oriented programming language, vertex attributes might be represented as instance variables
within a subclass of a Vertex class.

22.1 Breadth-first search

Breadth-first search is one of the simplest algorithms for searching a graph and archetype for many important graph
algorithms. Prim's minimum spanning tree algorithm and Dijstra's single source shortest paths algorithm use ideas
similar to those in breadth first search.

Given a graph G = (V, E) and a distinguished source vertex s, breadth first search systematically explores the edges
of G to "discover" every vertex that is reachable from s. It computes the distance (smallest number of edges) from s to
each reachable vertex. It also produces a breadth first tree with root s that contains all reachable vertices. For any
vertex v reachable from s, the simple path in the breadth-first tree from s to v corresponds to a 'shortest path' from
s to v in G, that is, a path containing the smallest number of edges, The algorithm works on both directed and
undirected graphs.

Breadth first search is so named because it expands the frontier between discovered and undiscovered vertices
uniformly across the breadth of the frontier. That is , the algorithm discovers all vertices at distance k from s
before discovering any vertices t distance K + 1.

To keep track of progress, breadth first search colors each vertex white, gray, or black. All vertices is discovered the
first time it is encountered during the search, at which time it becomes nonwhite. Gray and black vertices, therefore,
have been discovered, but breadth first search distinguishes between them eo ensure that the search proceeds in a
breadth first manner. If (u, v) < E and vertex u is black, then vertex v is either gray or black; that is all vertices
adjacent to black vertices have been discovered. Gray vertices may have some adjacent white vertices; they represent the
frontier between discovered and undiscovered vertices.

Breadth first search constructs a breadth first tree, initially containing only its root, which is the source vertex s,
whenever the search discovers a white vertex v in the course of scanning the adjacency list of an already discovered
vertex v in the course of scanning the adjacency list of an already discovered vertex u, the vertex v and the edge
(u, v) are added to the tree, We say tht u is the predecessor or parent of v in the breadth first tree. Since a vertex
is discovered at most once, it has at most one parent. Ancestor and descendant relationships in the breadth first tree
are defined relative to the root s as usual: if u is on the simple path in the tree from the root s to vertex v, then u
is an ancestor of v and v is a descendant of u.

The breadth first search procedure BFS below assumes that the input graph G = (V, E) is represented using adjacency
lists. it attaches several additional attributes to each vertex in the graph. We store the color of each vertex u < V
in the attribute u.color and the predecessor of u in the attribute u.pi. If u has no predecessor (for example, if u = s
or u has not been discovered) hte nu.pi = Nil. The attribute u.d holds the distance from teh source to vertex u
computed by the algorithm. The algorithm also uses a first in first out queue Q to manage the set of gray vertices.

BFS(G, s)
    for each vertex u <- G.V - {s}
        u.color = white
        u.d = inf
        u.pi = Nil
    s.color = GRAY
    s.d = 0
    s.pi = Nil
    Q = set()
    Enqueue(Q, s)
    while Q != None
        u = DEQUEUE(Q)
        for each v <- G.adj[u]
            if v.color == WHITE
                v.color = GRAY
                v.d = u.d + 1
                v.pi = u
                ENQUEUE(Q, v)
        u.color = BLACK


22.3 Depth first search

The strategy followed by depth first search is, as its name implies, to search 'deeper' in the graph whenever possible.

"""