from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    def __init__(self):
        print(self.create_food())
        print(self.create_drink())

    @abstractmethod
    def create_food(self):
        pass

    @abstractmethod
    def create_drink(self):
        pass

class Food:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Drink:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class LunchFirst(AbstractFactory):
    """Первое меню"""
    def create_food(self):
        return Food("Суп")
    def create_drink(self):
        return Drink("Чай")

class LunchSecond(AbstractFactory):
    """2 меню"""
    def create_food(self):
        return Food("Пицца")

    def create_drink(self):
        return Drink("Кофе")


class FactoryMethod:
    @staticmethod
    def get_lunch(number_menu):
        match number_menu:
            case 1:
                return LunchFirst()
            case 2:
                return LunchSecond()

FactoryMethod.get_lunch(2)