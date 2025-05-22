from inheritance.Car import Car


class RaceCar(Car):
    def __init__(self,title,price,max_speed):
        super().__init__(title, price)
        self.max_speed = max_speed

    def get_info(self):
        return f"{super().get_info()}\nМаксимальная скорость: {self.max_speed}"