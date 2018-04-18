class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    def run(self):
        print("Dog is running...")

    def eat(self):
        print("Eating meet...")


class Cat(Animal):
    def run(self):
        print("Cat is running...")


dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(dog)
run_twice(cat)


class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly...")


run_twice(Tortoise())


class Timer(object):
    def run(self):
        print("Start...")


run_twice(Timer())