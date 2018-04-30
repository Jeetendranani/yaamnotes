"""
binary tree traversal solution

in this article, we will provide the recursive solution for the tree traversal methods we have mentioned. And talk about
the implementation of the iterative solution. finally, we will discuss the difference between them.

Iterative solution
There are several iterative solutions for tree traversal. One of the solutions is to use a stack to simulate the
recursion process.

Tacking pre-order traversal as an example, in each iteration, we pop one node from the stack and visit this node. Then
if this node has right child, push its right child into the stack, if this node has a left child, push its left child
into the stack, it is noteworthy that we push the right child first so that we can visit th left child first since the
nature of the stack is lifo (last in first out). after that, we can continue the next iteration until the stack is
empty.

complexity analysis
As we mentioned before, we can traverse a tree recursively to retrieve all the data in pre-order, in-order or post-order
The time complexity is O(n) because we visit each node exactly once. And the depth of the tree might be N in the worst
case. That is to say, the level of recursion might be at most N in worst case. therefore, taking system stack into
consideration, the space complexity is O(N) as well.

To be cautions, the complexity might different due to a different implementation. It is comparatively easy to do
traversal recursively but when the depth of the tree is too large, we might suffer from stack overflow problem. That's
one of the main reason why we want to solve this problem iteratively sometimes.

For the iterative solution, the time complexity is apparently the same with the recursion solution which is O(n). The
space complexity is also O(n) since in the worst case, we will have all the nodes in the stack. There are some other
solutions for iterative traversal can reduce the space complexity to O(1).
"""