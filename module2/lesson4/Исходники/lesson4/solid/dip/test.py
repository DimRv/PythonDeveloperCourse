from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def on(self):
       pass

    @abstractmethod
    def off(self):
        pass

class Car(Vehicle):
    def on(self):
        print("Алгоритм запуска двигателя")
    def off(self):
        print("Алгоритм выключения двигателя")

class ElectroCar(Vehicle):
    def on(self):
        print("Алгоритм запуска двигателя У электроавтомобиля")
    def off(self):
        print("Алгоритм выключения двигателя У электроавтомобиля")