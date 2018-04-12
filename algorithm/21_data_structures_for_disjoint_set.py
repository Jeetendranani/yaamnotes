"""
21. Data structures for disjoint sets

Some applications involve grouping n distinct elements into a collection of disjoint sets. These applications often
need to perform two operations in particular: finding the unique set that contains a given element and uniting two sets.
This chapter explores methods for maintaining a data structure that supports these operations.

Section 21.1 describes the operations supported by a disjoint-set data structure and presents a simple application. In
section 21.2, we look at a simple linked-list implementation for disjoint sets. Section 21.3 presents a more efficient
presentation using rooted trees. The running time using hte tree representation is theoretically super-linear, but for
all practical purpose it is linear. Section 21.4 defines and discusses a very quickly growing function ant tis very
slowly growing inverse, which appears in the running time of operations on the tree-based implementation, and them, by
a complex amortized analysis, proves an upper bound on the running time that is just barely super-linear.

21.1. Disjoint-set operations

A disjoint-set dta structure maintains a collection s = {s1, s2, ... sk,} of disjoint dynamic sets. We identify each
set by a representative, which is some member of the set. In some applications, it doesn't matter which member is used
as the representative; we care only the set between the requests, we get the same answer both times. Other applications
may require a pre-specified rule for choosing the representative, such as choosing the smallest member in the set
(assuming, of course, that the elements can be ordered).

As in the other dynamic-set implementations we have studied, we represent each element of a set by an object. Letting x
denote an object, we wish to support the following operations:

Make-Set(x) creates a new set whose only member (and thus representative is x. Since the set are disjoint, we require
that x not already be in some other set.

Union(x, y) unites the dynamic sets that contains x and y, say Sx and Sy, into a new set that is the union of these two
sets. We assume that the two sets are disjoint prior to the operation. The representative of the resulting set is any
member of Sx U Sy, although many implementations of Union specifically choose the representative of either Sx or Sy as
new representative. Since we require the sets in the collection to be disjoint, conceptually we destroy Sx and Sy,
removing them from teh collection S. In practice, we often absorb the elements of one of the sets into the other set.

Find-set(x) returns a pointer to the representative of the (unique) set contains x.

Throughout this chapter, we shall analyze the running times of disjoint-set data structure in terms of two parameters:
n, the number of make-set operations, m, the total number of make-set, union and find-set operations, Since the sets are
disjoint, each union operation reduce the number of sets by one. After n-1 union operations, therefore, only one set
remains. The number of Union operations is thus at most n-1. Note also that since the make-set operations are included
in the total number of operations m, we have n >= n. We assume that n make-set operations are the first n operation
preformed.

An application of disjoint-set data structures

One of the many applications of disjoint-set data structures arise in determining the components of an undirected graph.
Figure 21.1(a), for example, shows a graph with four connected components.

The procedure connected-components that follows use the disjoint-set operations to compute the connected components of
graph. Once connected-components has preprocessed the graph, the procedure same-component answers queries about whether
two vertices are in the same connected components. (In pseudocode, we denote the set of vertices of a graph G by G.V
and the set of edges by G.E)


connected-components(G)
    for each vertex v in G.V
        make-set(v)

    for each edge(u, v) in G.E
        if find-set(u) != find-set(v)
            union(u, v)

same-component(u, v)
    if find-set(u) == find-set(v)
        return True
    else
        return False


The procedure connected-components initially places each vertex v in its own set. Then, for each edge (u, v), it unites
the sets containing u and v. By Exercise 21.1-2, after processing all the edges, two vertices are in the same connected
components if and only if the corresponding objects are in the same set. Thus, connected-components computes sets in a
way that the procedure same-component can determine whether two vertices are in the same connected component. Figure
21.2(b) illustrates how connected-components computes the disjoint sets.

In an actual implementation of this connected-components algorithm, the representations of the graph and the disjoint
set data structure would need to reference each other. That is, an object representing a vertex would contain a pointer
to the corresponding disjoint-set object, and vice versa. These programming details depend on the implementation
language, and we do not address them further here.

"""