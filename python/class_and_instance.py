class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("{}: {}".format(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


randy = Student('Randy Li', 90)
lisa = Student('Lisa Simpson', 87)
randy.print_score()
lisa.print_score()
print(randy.name, randy.get_grade())
print(lisa.name, lisa.get_grade())