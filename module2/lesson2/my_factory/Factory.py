from Car import Car


class Factory:
    def __init__(self, title, products, money=100_000_000):
        self.title = title
        self.products = products
        self.money = money
        self.manufactured = {k: 0 for k in self.products.keys()}
        self.orders = []
        self.cars_to_dealer = []
        self.income = 0

    def __str__(self):
        return f"{self.title}"

    def get_statistic(self):
        result = f"{self} бюджет {self.money:,.2f} выпустил:\n"
        for k, v in self.manufactured.items():
            result += f"\t {k} выпушено {v}шт\n"
        return result

    def create_car(self, car):
        if car.title in self.products.keys():
            self.money -= self.products[car.title] * .8
            self.manufactured[car.title] += 1
            print(f"Произведен автомобиль {car}\n")
        else:
            print(f"Производство модели {car.title} не налажено")

    def return_order(self, order):
        """Возврат заказа дилеру"""
        order.dealer.orders.append(order)
        self.orders.pop(self.orders.index(order))

    def check_order(self, order):
        """Проверка заказа и списание средств если все верно"""
        money = 0
        for car_title, count in order.cars.items():
            if car_title in self.products:
                price = self.products[car_title] if order.dealer.age < 10 else self.products[car_title] * .9
                money += price * count
            else:
                print(f"Нет технической возможности изготовить автомобиль {car_title}. Переоформите заказ")
                self.return_order(order)
                return
        if money >= order.dealer.money:
            print("Не хватает средств на заказ. Переоформите заявку")
            self.return_order(order)
            return
        self.money += money
        order.dealer.money -= money
        print("Оплата заказа произведена")
        return True

    def start_order_production(self, order):
        if self.check_order(order):
            print("Запущено производство автомобилей по заказу")
            for car_title, count in order.cars.items():
                n = count
                while n > 0:
                    car = Car(car_title)
                    self.create_car(car)
                    self.cars_to_dealer.append(car)
                    n -= 1
            self.send_cars(order)

    def send_cars(self, order):
        for _ in range(len(self.cars_to_dealer)):
            order.dealer.cars.append(self.cars_to_dealer.pop())
        self.orders.pop()


if __name__ == "__main__":
    import Car

    auto_vaz = Factory("ООО 'АвтоВАЗ Тольятти'", {'Гранта': 1_000_000, 'Веста': 1_500_000})
    print(auto_vaz.get_statistic())
    auto_vaz.create_car(Car.Car("Гранта", 106, "МT"))
    auto_vaz.create_car(Car.Car("Веста", 116, "AT"))
    auto_vaz.create_car(Car.Car("Нива", 116, "AT"))
    print(auto_vaz.get_statistic())




