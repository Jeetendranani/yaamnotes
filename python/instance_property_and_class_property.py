class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print("Test Fail!")
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('Test Fail!')
    else:
        lisa = Student("Lisa")
        if Student.count != 2:
            print("Test Fail!")
        else:
            print("Students:", Student.count)
            print("Test Passed!")

