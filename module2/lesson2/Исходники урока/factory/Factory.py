from random import randint

from Car import Car


class Factory:
    def __init__(self,title_factory):
        self.title_factory = title_factory

    def create_car(self,title_car):
        """Создание автомобиля по заказу на основе параметра"""
        print(f"Завод приступил к созданию автомобиля {title_car}")
        car = Car(title_car, randint(1000, 5000))
        print(f"Завод {self.title_factory} изготовил автомобиль {title_car}")
        return car
