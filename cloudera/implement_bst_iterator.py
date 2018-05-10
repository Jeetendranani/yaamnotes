class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tree = TreeNode(1)


class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.data = []
        self._inorder(root)
        self.current = 0 if root else -1

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            self.data.append(root.val)
            self._inorder(root.right)

    def hasNext(self):
        return self.current != -1 and self.current < len(self.data)

    def next(self):
        temp = self.data[self.current]
        self.current += 1
        return temp


i, v = BSTIterator(tree), []
while i.hasNext():
    v.append(i.next())
print(v)