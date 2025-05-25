from abc import ABC, abstractmethod


class Coffee(ABC):
    def __init__(self):
        self.grind_coffee()
        self.make_coffee()
        self.pass_coffee()

    def grind_coffee(self):
        print("Перемалывание зерен")
    def pass_coffee(self):
        print("Ваш кофе готов")
    @abstractmethod
    def make_coffee(self):
        pass

class Cappuchino(Coffee):
    def make_coffee(self):
        print("Варим кофе и добавляем молоко")

class Americano(Coffee):
    def make_coffee(self):
        print("Варим кофе")

class Latte(Coffee):
    def make_coffee(self):
        print("Варим кофе и добавляем много-много молока")

class Factory:
    @staticmethod
    def factory_method(title_coffee):
        match title_coffee:
            case "Капучино":
                return Cappuchino()
            case "Латте":
                return Latte()
            case "Американо":
                return Americano()
            case _:
                print("Напиток не определен!")
class CoffeeStore:
    @staticmethod
    def make_order(title_coffee):
        coffee = Factory.factory_method(title_coffee)
        if coffee:
            print(f"Можете забрать свой {title_coffee}")

CoffeeStore.make_order("Американо")