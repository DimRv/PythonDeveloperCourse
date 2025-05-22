from random import randint


class Order:
    def __init__(self,count_cars,title_models,factory):
        self.factory = factory
        self.title_models = title_models
        self.count_cars = count_cars
        #фура, которую требуется заполнить автомобилями
        self.cars = []
        self.result_money = 0

    def start_order(self):
        """Запускаем заказ в работу. Цель - заполнить фуру автомобилями"""
        for _ in range(self.count_cars):
            #Создаем автомобиль
            new_car = self.factory.create_car(self.title_models[randint(0,len(self.title_models) - 1)])
            #Помещаем созданный автомобиль в фуру
            self.cars.append(new_car)
            self.result_money += new_car.price

    def show_info(self):
        for i,car in enumerate(self.cars,1):
            print(f"{i}) {car}")
