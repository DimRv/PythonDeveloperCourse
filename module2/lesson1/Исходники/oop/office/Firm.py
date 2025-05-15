from random import randint

from oop.office.Person import Person


class Firm:
    def __init__(self,title,director,positions):
        self.positions = positions
        self.persons = [director]
        self.title = title
        
    def show_info(self):
        """Вывод информации о компании"""
        print(f"В компании {self.title} работают: {len(self.persons)} сотрудников:")
        for man in self.persons:
            print(man)

    def add_person(self):
        """Устройство новых сотрудников на работу"""
        fio = input("Введите имя сотрудника")
        post = self.positions[randint(0,len(self.positions) - 1)]
        new_person = Person(fio,post)
        self.persons.append(new_person)

    def remove_person(self,id):
        for i,person in enumerate(self.persons):
            if person.id == id:
                print(f"Сотрудник {self.persons.pop(i).fio} уволен")
                break
        else:
            print('Сотрудника с указанным ID не существует!')

    def add_salary(self,id,size_bonus):
        for man in self.persons:
            if man.id == id:
                man.salary += size_bonus

