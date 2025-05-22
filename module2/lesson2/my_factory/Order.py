class Order:
    def __init__(self, dealer, cars):
        self.cars = cars
        self.dealer = dealer

    def __repr__(self):
        result = f"Заказ от {self.dealer.title}:\n"
        for k, v in self.cars.items():
            result += f'\t{k}: {v}шт\n'
        return result


if __name__ == "__main__":
    import Dealer
    dealer1 = Dealer.Dealer('ООО "Прагматика"', 10, 40_000_000)
    order = Order(dealer1, {"Веста": 2, "Нива": 5})
    print(order)
