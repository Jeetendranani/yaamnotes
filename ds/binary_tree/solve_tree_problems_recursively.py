"""
Solve tree problems recursively

    top down solution
    button up solution
    conclusion

In previous sections, we have introduced how to solve tree traversal problem recursively. Recursion is one of the most
powerful and frequent used methods for solving tree related problems.

As we know, a tree can be defined recursively as node (the root node), which includes a value and a list of references
to other nodes, recursion is one of the natures of the tree. Therefore, many tree problems can be solved recursively.
For each recursion level, we can only focus on the problem within one single node and call the function recursively to
solve its children.

Typically, we can solve a tree problem recursively from the top down or from teh bottom up.

Top down solution

Top down means that in each recursion level, we will visit the node first to come up with some values, and pass these
values to its children when calling the function recursively. So the top down solution can be considered as kind of
preorder traversal. To be specific, the recursion function top_down(root, params) works like this:
    1. return specific value for null node
    2. update the answer if needed
    3. left_ans = top_down(root.left, left_params)
    4. right_ans = top_down(root.right, right_params)
    5. return the ans if needed
For instance, consider this problem: Given a binary tree, find its maximum depth.

We know that the depth of the root nodes is 1. For each node, if we know the depth of the node, we will know the depth
of its children. Therefore, if we pass the depth of the node as parameter when calling the function recursively, all
the nodes know the depth fo themselves, and for leaf nodes, we can use the depth to update the final answer, Here is
the pseudocode for the recursion function maximum_depth(root, depth):
    1. return if root is null
    2. if root is a leaf node:
    3.      answer = max(answer, depth)
    4. maximum_depth(root.left, depth + 1)
    5. maximum_depth(root.right, depth + 1)

bottom up solution
bottom up is another recursion solution. In each recursion level, we will firstly call teh functions recursively for
all the children nodes and then come up with the answer according to the return values and the value of the root node
itself. This process can be regarded as kind of postorder traversal. Typically, a "bottom up" recursion function
bottom_up(root) will be like this:
    1. return specific value of null node
    2. left_ans = bottom_up(root.left)
    3. right_ans = bottom_up(root.right)
    4. return answers

let's go on discussing the question about maximum depth but using a different way of thinking: for a single node of the
tree, what will be the maximum depth x of the subtree rooted as itself?

If we know the maximum depth l of the subtree rooted at its left child and the maximum depth r of the subtree rooted at
its right child, can we answer the previous question? Of course yes, we can choose the maximum between them and pus 1
to get maximum depth of the subtree rooted at the selected node. That is x = max(l, r) + 1.

It means that for each node, we can get the answer after solving the problem of tis children. Therefore, we can solve
this problem using a bottom-up solution. Here is the pseudocode for the recursion function maximum_depth(root):
    1. return 0 if root is null
    2. left_depth = maximum(root.left)
    3. right_depth = maximum(root.right)
    4. return max(left_depth, right_depth) + 1

It is not eay to understand recursion and find out a recursion solution for the problem.

When you meet a tree problem, ask yourself two questions: can you determine some parameters to help the node know the
answer of itself? can you use these parameters and the value of the node itself to determine what should be the
parameters parsing to its children? If the answers are both yes, try solve this problem using a top down recursion
solution.

Or you can think the problem in this way: for a node in a tree, if you know the answer of its children, can you
calculate teh answer of teh node? if the answer is yes, solving the problem recursively from bottom up might be a good
way.

In the following sections, we provide several classic problems for you to help you understand tree structure and
recursion better.
"""
