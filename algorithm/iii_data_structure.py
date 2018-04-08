"""
III. Data Structures

Introduction

Sets are as fundamental to computer science as they are to mathematics. Whereas mathematical sets are unchanging, the
sets manipulated by algorithms can grow, shrink, or otherwise change over time.  We call such set dynamic. The next
five chapters present some basic techniques for representing finite dynamic sets and manipulating them on a computer.

Algorithms may require several different types of operations to be performed on sets. For example, many algorithms need
only the ability to insert element into, delete element from, and test membership in a set. We call a dynamic set that
supports these operations a dictionary. Other algorithms require more complicated operations. For example, min-priority
queues, which chapter 6 introduced in the context of the heap data structure, support the operations of inserting an
element into and extracting the smallest element from a set. The best way to implement a dynamic set depends upon the
operations that must be supported.

Elements of a dynamic set

In a typical implementation of a dynamic set, each element is represented by an object whose attributes can be examined
and manipulated if we have a pointer to teh object. (Section 10.3 discusses the implementation of objects and pointers
in programming environments that do not contain them as basic data types.) Some kinds of dynamic sets assume that one
of the objects's attributes is an identifying key. If the keys are all different, we can think of the dynamic set as
being a set of key values. The object may contain satellite data, which are carried around in other object attributes
but otherwise unused by the set implementation. It may also have attributes that are manipulated by the set operations;
these attributes may contain data or pointers to other objects in teh set.

Some dynamic sets presuppose that the keys are draw from a totally ordered set. Such as the real numbers, or the set of
all words under the usual alphabetic ordering. A total ordering allows us to define the minimum element of the set, for
example, or to speak of the next element garger than a given element in a set.

Operations on dynamic sets

Operations on a dynamic set can be grouped into two categories: queries, which simply return information about the set,
and modifying operations, which change the set. Here is a list of typical operations. Any specific application will
usually require only a few of these to be implemented.

Search(S, k)
    A query that, given a set S and a key value k, return a pointer x to an element in S such that x.key = k, or nil if
    no such element belongs to S.

Insert(S, x)
    A modifying operation that augments the set S wilt the element pointed to by x. We usually assume that any
    attributes in element x needed by the set implementation have already been initialized.

Delete(S, x)
    A modifying operation that, given a pointer x to an element in the set S, removes x from S.

Minimum(S)
    A query on the totally ordered set S that returns a pointer to the element of S with the smallest key.

Maximum(S)
    A query on a totally ordered set S that returns a pointer to the element ot S with the largest key.

Successor(S, x)
    A query that, given an element x whose key is from a totally ordered set S, return a pointer to the next larger
    element in S, or nil if x is the maximum element.

Predecessor(S, x)
    A query that, given an element x whose key is from a totally ordered set S, returns a pointer to the next smaller
    element in S, or nil if x is the minimum element.

In some situations, we can extend the queries successor and predecessor so that they apply to sets with non-distinct
keys. For a set on n keys, the normal presumption is that a call to minimum in the set in sorted order.

We usually measure the time take to execute a set operation in terms of the size of the set. For example, chapter 13
describes a data structure that can support any of operations listed above on the set of size n in time O(lgn).
"""