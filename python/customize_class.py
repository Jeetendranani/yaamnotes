class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Student object (name: {})".format(self.__name)

    __repr__ = __str__


print(Student('Randy'))

s = Student('Randy')
print(s)


class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > 1000000:
            raise StopIteration()
        return self.__a


for n in Fib():
    print(n)


class Fib1(object):
    def __init__(self):
        self.__a, self.__b = 1, 1

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop

            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b

            return L


f = Fib1()
print(f[3])
print(f[5:9])


class Student1(object):
    def __init__(self):
        self.__name = 'Randy'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError("Student object has no attribute '{}'.".format(attr))


s = Student1()
print(s.score)
print(s.age())
# s.abc


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain("{}/{}".format(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("My name is {}.".format(self.name))


s = Student2("Randy")
s()

print(callable(s))