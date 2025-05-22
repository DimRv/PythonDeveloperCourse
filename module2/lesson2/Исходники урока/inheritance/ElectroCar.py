from inheritance.Car import Car


class ElectroCar(Car):
    def __init__(self,title,price,battery_power):
        super().__init__(title, price)
        self.battery_power = battery_power


    def get_info(self):
        return f"{super().get_info()}\nБатарея заряжена на: {self.battery_power}%"