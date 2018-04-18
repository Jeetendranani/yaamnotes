class Student(object):
    def __init__(self):
        self.__score = None

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self.__score = value


s = Student()
s.set_score(60)
print(s.get_score())
# s.set_score(9999)
# s.set_score('1')


class Student1(object):
    def __init__(self):
        self.__score = None
        self.__birth = None

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 1 - 100!')
        self.__score = value

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2018 - self.__birth


