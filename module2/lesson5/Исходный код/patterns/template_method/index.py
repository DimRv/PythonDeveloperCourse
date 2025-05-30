from abc import ABC, abstractmethod


class Education(ABC):
    def study(self):
        self.income()
        self.learn()
        self.pass_exams()
        self.get_doc()

    @abstractmethod
    def income(self):
        pass

    @abstractmethod
    def learn(self):
        pass

    def pass_exams(self):
        print("Сдача экзаменов")
    @abstractmethod
    def get_doc(self):
        pass

class School(Education):
    def income(self):
        print("Поступление без экзаменов")

    def learn(self):
        print("Посещаем уроки и делаем ДЗ")

    def get_doc(self):
        print("Получаем аттестат об образовании")



class Univer(Education):
    def income(self):
        print("Поступление после успешной сдачи экзаменов")

    def learn(self):
        print("Посещаем лекции и практику")

    def get_doc(self):
        print("Получаем диплом об образовании")

my_school = School()
my_univer = Univer()
for item in my_school, my_univer:
    item.study()
    print("*"*50)