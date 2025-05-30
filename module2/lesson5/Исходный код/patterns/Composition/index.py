from abc import ABC, abstractmethod


class SimpleGraphic(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(SimpleGraphic):
    def draw(self):
        print("Рисуем прямую линию")


class Rectangle(SimpleGraphic):
    def draw(self):
        print("Рисуем прямоугольник")

class House(SimpleGraphic):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def draw(self):
        for item in self.items:
            item.draw()
        print("Дом построен")

line_first = Line()
line_second = Line()
rectangle = Rectangle()

house = House()
house.add_item(line_first)
house.add_item(line_second)
house.add_item(rectangle)
house.draw()