class Car:
    def __init__(self, title, color, price, engine, gearbox):
        self.gearbox = gearbox
        self.engine = engine
        self.price = price
        self.color = color
        self.title = title
        self.discount = 0

    def __str__(self):
        return f"{self.title} {self.color} {self.get_price()}руб:\n\t {self.engine} {self.gearbox}"

    def set_discount(self, discount):
        self.discount = discount if 0 < discount < 100 else 0

    def get_price(self):
        return format(self.price - self.price * self.discount / 100, '.2f')

