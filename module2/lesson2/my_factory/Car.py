from datetime import datetime


class Car:
    def __init__(self, title, engine=106, transmission='AT', year=datetime.now().year):
        self.title = title
        self.engine = engine
        self.transmission = transmission
        self.year = year

    def __repr__(self):
        return f'{self.title} {self.engine}л.с. {self.transmission} {self.year} года выпуска'


if __name__ == '__main__':
    car1 = Car('Веста', 106, 'МТ')
    car2 = Car('Нива', 116, "AT", 2023)
    print(car1)
    print(car2)