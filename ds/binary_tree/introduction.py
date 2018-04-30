"""
Introduction

A tree is a frequently-used data structure to simulate a hierarchical tree structure. Each node of the tree will have a
root value and a list of references to other nodes which are called child nodes. From graph view, a tree can also be
defined as a directed acyclic graph which has n nodes and n-1 vertices.

A binary tree is one of teh most typical tree structure, as the name suggests, a binary tree is a tree data structure
in which each node has at most two children, which are referred as teh left child and right child.

By completing this card, you will be able to:
    1. Understand teh concept of a tree and a binary tree;
    2. Be familiar with different traversal methods;
    3. Use recursion to solve binary tree related problems;

Traverse a Tree

In the introduction, we have gone through the concept of a tree and a binary tree.

In this chapter, we will focus on the traversal methods used in a binary tree. Understanding these traversal methods
will definitely help you have a better understanding of the tree structure and have a solid foundation for the further
study.

The goal of hte chapter is to:
    1. understand the difference between different tree traversal methods;
    2. Be able to solve pre-order, in-order and post-order traversal recursively;
    3. Be able to solve pre-order, in-order and post-order traversal iteratively;
    4. Be able to do level traversal using BFS.

A traverse a tree - introduction

    pre-order traversal
    in-order traversal
    post-order traversal
    recursive or iterative

pre-order traversal
pre-order traversal is to visit the root first. then traversal the left subtree. finally, traverse the right subtree.

in-order traversal
in-order traversal is to traversal the left subtree first, then visit the root, finally, traverse the right subtree.
Typically, for binary search tree, we can retrieve all the data in sorted order using in-order traversal. we will
mention that again in other card (introduction to data structure - binary search tree).

post order traversal
post order traversal is to traverse the left subtree first, then the right subtree, finally, visit the root.

It is worth nothing that when you delete nodes in a tree, deletion process will be in post-order. that is to say, when
you delete a node, you will delete its left child and its right child before you delete the node itself.

Also, post-order is widely use in mathematical expression. it is easier to write a program to parse a post-order
expression.

You can easily figure out the original expression using the inorder traversal, however, it is not easy for program to
handle this expression since you have to check the priorities of operations.

if you have handle this tree in post-order,you can easily handle the expression using a stack, each time when you meet
a operator, you can just pop2 elements from teh stack, calculate the result and push the result back into the stack.

Recursive or iterative
Try to practice the tree different traversal methods in our after-article exercise, you might want to implement the
methods recursively or iteratively. implement both recursion and iteration solution and compare the difference between
them.
"""