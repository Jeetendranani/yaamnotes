class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog1(Mammal, Runnable):
    pass


class Bat1(Mammal, Flyable):
    pass


class RunnableMixIn(object):
    pass


class FlyableMixIn(object):
    pass


class CarnivorousMixIn(object):
    pass


class HerbivoresMixIn(object):
    pass


class Dog2(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


class TCPServer(object):
    pass


class ForkingMixIn(object):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class UDPServer(object):
    pass


class ThreadingMixIn(object):
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


class CoroutineMinIn(object):
    pass


class MyTCPServer1(TCPServer, CoroutineMinIn):
    pass