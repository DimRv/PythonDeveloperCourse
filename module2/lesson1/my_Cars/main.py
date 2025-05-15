

from Car import Car
from Engine import Engine
from GearBox import Gearbox
from random import choice, randint


car_title = ['BMW', 'Volvo', "Audi"]
car_color = ['Черный', "Красный", "Белый"]

car1 = Car(
    choice(car_title),
    choice(car_color),
    randint(5, 7) * 1_000_000,
    Engine("Бензиновый", 2.5, randint(100, 250)),
    Gearbox("Автоматическая")
)

car2 = Car(
    choice(car_title),
    choice(car_color),
    randint(5, 7) * 1_000_000,
    Engine("Бензиновый", 2.2, randint(100, 250)),
    Gearbox("Механическая")
)

car3 = Car(
    choice(car_title),
    choice(car_color),
    randint(5, 7) * 1_000_000,
    Engine("Гибрид", 2.8, randint(100, 250)),
    Gearbox("Автоматическая")
)

print(f"До скидки:".center(40, "-"))
for car in (car1, car2, car3):
    print(car)

car2.set_discount(10)
car3.set_discount(15)

print(f"После скидки:".center(40, "-"))
for car in (car1, car2, car3):
    print(car)