"""
Introduction

This part returns to studying data structures that support operations on dynamic sets, but at a more advanced level
than part III. two of the chapters, for example, make extensive use of the amortized analysis techniques we saw in
chapter 17.

Chapter 18 presents b-trees, which are balanced search trees specifically designed to be stored on disks. because disks
operate much more slowly than random-access memory, we measure the performance of b-trees not only by how much computing
time the dynamic-set operations consume but also by how many disk accesses they perform. For each b-tree operation, the
number of disk accesses increases with the height of the b-tree, but b-tree operations kep the height low.

Chapter 19 geives an implementation of a merge-able heap, which supports the operations insert, minimum, extract-min
and union. The union operation unites, or merges two heaps. Fibonacci heaps - the data structure in chapter 19 - also
support the operations delete and decrease-key. We use amortized time bounds to measure the performance of Fibonacci
heaps. The operations insert, minimum, and union take only O(1) actual and amortized time of Fibonacci heaps, and
operations extract-min and delete take O(lgn) amortized time. the most significant advantage of Fibonacci heaps,
however, is that decrease-key takes only O(1) amortized time. Because the decrease-key operation takes constant
amortized time, Fibonacci heaps are key component of some of the asymptotically fastest algorithms to date for the
graph problems.

Noting that we can beat the M(nlgn) lower bound for sorting when the keys are integers in a restricted range, chapter 20
asks whether we can design a data structure that supports the dynamic-set operations search, insert, delete, minimum,
maximum, successor, and predecessor in O(lgn) time when the key are integers in a restricted range. The answer turns
out to be that we can, by usign integers drawn from the set {0, 1, 2, .. u-1}, where u is an exact power of 2, then van
Emde Boas tree support each of the above operations in O(lg lgu) time.

Finally, chapter 21 presents data structures for disjoint sets. we have a universe of n elements that are partitioned
into dynamic sets. Initially, each element belongs to its own singleton set. The operation Union unites two sets, and
the query find-set identifies the unique set that contains a given element at the moment. By representing each set as
single rooted tree, we obtain surprisingly fast operations: a sequence of m operations runs in O(m a(n)) time, where
a(n) is an incredibly slowly growing function - a(n) is at most 4 in and conceivable application. The amortized analysis
that proves this time bound is as complex as the data structure is simple.

The topics covered in this part are by no means the only examples of 'advanced' data structures. Other advanced data
structures including the following:

    - Dynamic trees, introduced by Sleator and Tarjan and discussed by Tarjan, maintain a forest of disjoint rooted
    tree. Each edge in each tree has a real-valued cost. Dynamic trees support queries to find parents, roots, edge
    costs, and the minimum edge cost on a simple path from a node up to a root. Trees may be manipulated by cutting
    edges, updating all edge costs on a simple path from a node up to a root, linking a root into another tree, and
    making a node from the root of the tree it appears in. One implementation of dynamic trees gives an O(lgn)
    amortized time bound for each operations; a more complicated implementation yields O(lg n) worst-case time bounds.
    Dynamic trees are used in some of the asymptotically fastest networ-flow algorithms

    - splay trees, developed by Sleator and Tarjan and again discussed by Tarjan, are a form of binary search tree on
    which the standard search tree operations run in O(lgn) amortized time. One application of splay trees simplifies
    dynamic trees.

    - persistent data structures allow queries, and sometimes updates as well, on pat version of a data structure.
    Driscoll, Sarnak, Sleator, and Tarjan persent techniques for making linked data structures persistent with only a
    small time and space cost. Problem 13-1 gives a simple example of a persistent dynamic set.

"""