from Factory import Factory
from Car import Car
from Dealer import Dealer
from Order import Order


auto_vaz = Factory("ООО 'АвтоВАЗ Тольятти'", {'Гранта': 1_000_000, 'Веста': 1_500_000})
print(auto_vaz.get_statistic())
auto_vaz.create_car(Car('Гранта'))
auto_vaz.create_car(Car('Веста'))
print(auto_vaz.get_statistic())

dealer = Dealer("ООО 'Прагматика'", 20, 30_000_000)
print(dealer.get_statistic())

dealer.create_order(Order(dealer, {'Веста': 2, 'Гранта': 3}))
dealer.create_order(Order(dealer, {'Веста': 3, 'Нива': 4}))
print(dealer.orders)

dealer.send_order(0, auto_vaz)
print(dealer.orders)
print(auto_vaz.orders)

auto_vaz.start_order_production(auto_vaz.orders[0])
print(auto_vaz.get_statistic())
print(dealer.get_statistic())

dealer.sell_car(0, 1_200_000)
dealer.sell_car(3, 1_800_000)
print(dealer.get_statistic())

dealer.send_order(0, auto_vaz)
auto_vaz.start_order_production(auto_vaz.orders[0])
print(dealer.orders)
