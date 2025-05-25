class Person:
    def __init__(self,fio):
        self.fio = fio
    def work(self):
        return f"{self.fio} ходит на работу"

class Manager(Person):
    def work(self):
        return f"{super().work()}, управляет коллективом..."

class Company:
    def get_info(self,person:Person):
        return person.work()

person = Person("Иван")

manager = Manager("Иван")

company = Company()
company.get_info(manager)

men = [person,manager]
