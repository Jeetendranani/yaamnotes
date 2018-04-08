"""
12. Binary Search Trees

The search tree data structure supports many dynamic-set operations, including search, minimum, maximum, predecessor,
successor, insert, and delete. Thus, we can use a search tree both as a dictionary and as a priority queue.

Basic operations on a binary search tree take time proportional to the height of the tree. For a complete binary tree
with n nodes, such operations run in O1(lgn) worst-case time. If the tree is a linear chain of n nodes, however, the
same operations take O1)n) worst-case time. We shall see in section 12.4 that the expected height of a randomly built
binary search tree is O(lgn), so that basic dynamic-set operations on such a tree take O1(lng) time on average.

In practice, we can't always guarantee that binary search trees are built randomly, but we can design variations of
binary search trees with good guaranteed worst-case performance on basic operations. chapter 13 will present one such
variation, red-black trees, which have height O(lgn). Chapter 18 introduces B-trees, which are particularly good for
maintaining databases on secondary (disk) storage.

After presenting the basic properties of binary search trees, the following sections show how to work binary search tree
to print its values in sorted order. how to search for a value in a binary search tree, how to find the minimum or
maximum element, how to find the predecessor and successor of an element, and how to insert into or delete from a
binary search tree. The basic mathematical properties of trees appear in Appendix B.

12.1 What is a binary search tree?

a binary search tree is organized, as the name suggests, in a binary search tree, as show in Figure 12.1. We can
represent such a tree by a linked ata structure in which each node is an object. In addition to a key and satellite data
each node contains attributes left, right, and p that point to the nodes corresponding to its left child, right child,
and its parent, respectively. If a child or the parent is missing, the appropriate attribute contains the value Nil. the
root node is hte only node in the tree whose parent is Nil.

The keys in a binary search tree are always stored in such a way as to satisfy the binary-search-tree property:
    Let x be a node in a binary search tree. If y is a node in the left subtree of x, then y.key <= x.key, if y is a
    node in the right subtree of x, then y.key >= x.key.


Successor and predecessor

Given a node in a binary search tree, sometimes we need to find its successor in the sorted order determined by an
inorder tree walk. If all keys are distinct, the successor of a node x is the node with the smallest key greater than
x.key. the structure of binary tree allows us to determine the successor of a node without ever comparing keys. The
following procedure returns the successor of a node x in a binary search tree if it exists, and Nil if x has the largest
key in the tree.

tree-successor(x)
    if x.right != Nil
        return tree-minimum(x, right)
    y = x.p
    while y != nil and x == y.right
        x = y
        y = y.p
    return y

12.3. Insertion and deletion

The operations of insertion and deletion cause the dynamic set represented by a binary search tree to change. The data
structure must be modified to reflect this change, but in such a way that the binary-search-tree property continues to
hold. As we shall see, modifying the tree to insert a new element is relatively straightforward, but handling deletion
is somewhat more intricate.

Insertion

To insert a new value v into a binary search tree T, we use the procedure tree-insert. The procedure takes a node z for
which z.key = v, z.left = Nil, and z.right = Nil. It modifies T and some of the attributes of z in such a way that it
inserts z into an appropriate position in the tree.

tree-insert(T, z)
    y = Nil
    x = T.root
    while x != Nil
        y = x
        if z.key < x.key
            x = x.left
        else
            x = x.right
    z.p = y
    if y == Nil
        T.root = z
    elseif z.key < y.key
        y.left = z
    else
        y.right = z
"""