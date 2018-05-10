# -*- coding: utf-8 -*-
# implement_bst_iterator_oh.py


class BSTIterator(object):
    def __init__(self, root):
        self.treeStack = []
        while root:
            self.treeStack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.treeStack) != 0

    def next(self):
        node = self.treeStack.pop()
        if node.right is not None:
            node2 = node.right
            while node2:
                self.treeStack.append(node2)
                node2 = node2.left
        return node.val