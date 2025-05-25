from abc import ABC
from typing import Generic, TypeVar,List

# Создаем абстрактный тип данных, который будет конкретизирован при реализации

T = TypeVar('T')
#
# class Test(Generic[T]):
#     def __init__(self,content: T):
#         self.content = content
#
# obj1: Test[int] = Test(5.3)
# obj2: Test[str] = Test("demo")
# class Car(Generic[T]):
#     def __init__(self,engine: T):
#         self.engine = engine


# Пример №2

# class Parking(Generic[T]):
#     def __init__(self):
#         self.parking:List[T] = []
#
#     def add_car(self,car:T)->None:
#         self.parking.append(car)
#     def remove_car(self)->None:
#         self.parking.pop()
#
# my_parking = Parking[str]()
# my_parking.add_car("Audi")
# my_parking.add_car("BMW")

class Car:
    def __init__(self,title):
        self.title = title

class Parking(ABC,Generic[T]):
    @abstractmethod
    def get_car(self,id:int) ->T:
        pass
    def get_cars(self) ->List[T]:
        pass
    
class MyParking(Parking[Car]):
    def __init__(self):
        self.places = {}
    def get_car(self,id:int) ->Car:
        return self.places[id]
    def get_cars(self) ->List[Car]:
        return list(self.places.values())