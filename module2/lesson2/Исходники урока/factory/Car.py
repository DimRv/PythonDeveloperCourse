class Car:
    def __init__(self, title, price):
        self.price = price
        self.title = title

    def __str__(self):
        return f"Автомобиль {self.title} стоит {self.price}"
