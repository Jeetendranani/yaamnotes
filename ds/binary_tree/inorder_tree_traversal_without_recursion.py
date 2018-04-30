"""
Inorder tree traversal without recursion

Using stack is the obvious way to traverse tree without recursion. Below is an algorithm for traversing binary tree
using stack, see this for step wise step execution of the algorithm.

1. create an empty stack s.
2. initialize current node as root
3. push the current node to s and set current = current left until current is null
4. if current is null and stack is not empty then
    a. pop the top item from stack
    b. print the popped item, set current = popped_item -> right.
    c. go to step 3
5. if current is null and stack is empty then we are done

let us consider the below tree for example

                    1
                   /  \
                  2    3
                 / \
                4   5

step 1 create an empty stack: s = null

step 2 set current as address of root: current -> 1

step 3 pushes the current node and set current = current -> left until current is null

    current -> 1
    push 1: stack s -> 1
    current -> 2
    push 2: stack s -> 2, 1
    current -> 4
    push 4: stack s -> 4, 2, 1
    current = NULL

step 4 pop from s
    a. pop 4: stack s -> 2, 1
    b. print "4"
    c. current = NULL /*right of 4*/ and go to step 3
Since current is NULL step 3 doesn't do any thing.

step 4 again:
    a. pop 2: stack -> 1
    b. print "2"
    c. current -> 5 /*right of 5 */ and go to step 3

step 3 pushes 5 to stack and makes current NULL
    stack s -> 5, 1
    current = NULL

step 4 pops from S
    a. pop 5: stack s -> 1
    b. print "5"
    c. current = NULL /*right of 5*/ and go to step 3
Since current is NULL step 3 doesn't do anything

step 4 pops again
    a. pop 1: s -> NULL
    b. print "1"
    c. current -> 3 ?*right of 5*/

step 3 pushes 3 to stack and makes current NULL
    stack s -> 3
    current - NULL

step4 pops from s
    a. pop 3: stack s -> NULL
    b. print "3"
    c. current = NULL /*right of 3*/

Traversal is done now as stack s is empty and current is NULL.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    current = root
    s = []
    done = 0

    while not done:
        if current:
            s.append(current)
            current = current.left

        else:
            if s:
                current = s.pop()
                print(current.data)
                current = current.right
            else:
                done = 1
