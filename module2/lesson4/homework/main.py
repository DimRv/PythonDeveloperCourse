"""
Создать проект Автомобиль у которого есть два составляющих элемента:это кузов и двигатель,
а также у авто есть свойство isEngine - оно отвечает за запуск двигателя.
У класса Car создайте два метода - запустить двигатель и заглушить.
В методах проверяйте состояние автомобиля, то есть не нужно запускать работающий автомобиль.
Вывести информацию о свойствах автомобиля - цвет кузова, объем двигателя и другое,
а также его состояние (вкл или выкл)
"""

from Car import Car
from Body import Body
from Engine import Engine


car1 = Car("Веста").add_engine(Engine('Бензиновый')).add_body(Body("Седан", "черный"))
car2 = Car("Тесла").add_engine(Engine('Электрический'))
car3 = Car("Буханка")

for car in car1, car2, car3:
    car.start_engine()
    car.stop_engine()
    print(car.get_info())


