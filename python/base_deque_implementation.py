class deque(object):
    def __init__(self, iterable=(), maxsize=-1):
        if not hasattr(self, 'data'):
            self.left = self.right = 0
            self.data = {}
        self.maxsize = maxsize
        self.extend(iterable)

    def extend(self, iterable):
        for elem in iterable:
            self.append(elem)

    def append(self, x):
        self.data[self.right] = x
        self.right +=1
        if self.maxsize != -1 and len(self) > self.maxsize:
            self.popleft()

