"""
Iterative post order traversal

We have discussed iterative inorder and iterative preorder traversals. In this post, iterative postorder traversal is
discussed which is more complex than the other two traversals (due to its nature of non-tail recursion, there is an
extra statement after the final recursive call to itself). The postorder traversal can easily be done using two stacks
though. The idea is to push reverse postorder traversal to a stack. Once we have reverse postorder traversal in a stack,
we can just pop all items one by one from the stack and print them. this order of printing will be in postorder because
of LIFO property of stacks. Now the question is, how to get reverse post order elements in a stack - the other stack is
used for this purpose. for example, in the follow tree, we need to get 1,3,7,6,2,5,4 in a stack. If take a close look
at this sequence, we can observe that this sequence is very similar to preorder traversal. The only difference is right
child is visited before left child and therefore sequence is "root right left" instead of "root left, right". So we can
do something like iterative preorder traversal with following differences.

a. instead of print an item, we push it to a stack.
b. we push left subtree before right subtree.

Following is the complete algorithm. After step2, we get reverse postorder traversal in second stack, we use first stack
to get this order.

1. Push root to first stack
2. loop while first stack is not empty
    2.1 pop a node from first stack and push it to teh second stack
    2.2 push left an right children of the popped node to first stack
3. print contents of second stack

Let us consider the following tree

                1
               /  \
              2    3
             / \  / \
            4  5 6  7

Following are teh steps to print postorder traversal of the above tree using two stacks.

1. Push 1 to fist stack.
    first stack: 1
    second stack: empty

2. Pop 1 from first stack and push it to second stack.
    push left and right child of 1 to first stack
    first stack: 2. 3,
    second stack: 1

3. Pop 3 from first stack and push it to second stack.
    push left and right children of 3 to the second stack.
    First stack: 2, 6, 7
    second stack: 1, 3

4. Pop 7 from first stack and push it to second stack.
    first stack: 2, 6
    second stack: 1, 3, 7

5. Pop 6 from first stack and push it to second stack.
    first stack: 2
    second stack: 1, 3, 7, 6

6. pop 2 from first stack and push it to second stack.
    Push left and right children of 2 to first stack
    first stack: 4, 5
    second stack 1, 3, 7, 6, 2

7. pop 5 from first stack and push it to second stack.
    first stack: 4
    second stack: 1, 3, 7, 6, 2, 5

8. Pop 4 from first stack and push it to second stack.
    first stack: empty
    second stack: 1, 3, 7, 6, 2, 5, 4

The algorithm stops since there is no more item in first stack.
Observe that content of second stack is in postorder fashion, print them.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def post_order_iterative(root):
    if root is None:
        return

    s1 = []
    s2 = []

    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        node = s2.pop()
        print(node.data)