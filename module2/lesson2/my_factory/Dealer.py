class Dealer:

    def __init__(self, title, age, money):
        self.age = age
        self.title = title
        self.money = money
        self.cars = []
        self.sold_cars = 0
        self.orders = []

    def __str__(self):
        return self.title

    def get_statistic(self):
        result = f"{self} {self.age} лет работы, продано {self.sold_cars} автомобилей, бюджет {self.money:,.2f}руб\n"
        if self.cars:
            result += 'Содержит автомобили на продажу:\n'
            for car in self.cars:
                result += f'\t{car}\n'
        else:
            result += 'Не имеет автомобилей на продажу'
        return result

    def create_order(self, order):
        print("Создан заказ")
        self.orders.append(order)

    def send_order(self, index, factory):
        order = self.orders.pop(index)
        factory.orders.append(order)
        print(f"Заказ от {self.title} передан {factory.title}")

    def sell_car(self, i, money):
        self.money += money
        car = self.cars.pop(i)
        self.sold_cars += 1
        print(f'Продан автомобиль {car}')


if __name__ == '__main__':
    d1 = Dealer("ООО 'ПитерАвто'", 5, 20_000_000)
    print(d1)
