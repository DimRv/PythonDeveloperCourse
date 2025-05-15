from oop.office.Firm import Firm
from oop.office.Person import Person
from oop.office.Position import Position

position1 = Position(1,"Программист",200_000)
position2 = Position(2,"DevOps",220_000)
position3 = Position(3,"Директор",600_000)

director = Person("Романов",position3)

firm = Firm("IT Start",director,[position1,position2])

"""Устраиваем на работу трех сотрудников"""
for _ in range(3):
    firm.add_person()

"""Увольняем сотрудника с ID = 2"""
# firm.remove_person(2)

"""Добавим оклад сотруднику с ID = 3"""
firm.add_salary(3,50_000)
"""Выводим оставшихся сотрудников"""
firm.show_info()