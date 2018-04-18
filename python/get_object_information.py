import types


print(type(123))
print(type('str'))
print(type(None))
print(type(abs))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)


class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))

print(isinstance(d, Husky))
print(isinstance(d, Dog))
print(isinstance(d, Animal))


class MyDog(object):
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

print(dir(dog))

print(hasattr(dog, 'x'))
print(dog.x)

print(hasattr(dog, 'y'))
setattr(dog, 'y', 19)
print(hasattr(dog, 'y'))
print(getattr(dog, 'y'))
print(dog.y)


def read_image(fp):
    if hasattr(fp, 'read'):
        return read_data(fp)
    return None


def read_data(fp):
    pass
