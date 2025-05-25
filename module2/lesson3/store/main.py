"""Цель - создать консольный магазин
1) Создать класс Item. Это описание каждого товара в каталоге
2) Создать класс Каталог товаров, который выводи все товары в консоль и в этом классе будет метод
для добавления товара в корзину
3) Создать класс Товар корзины. Это помок класса Товар каталога, т.к. у товара корзины все те же свойства,
плюс количество добавленных этого типа товаров
4) Класс Корзина - вывести список товаров корзины с учетом количества"""
from Cart import Cart
from Catalog import Catalog
from Category import Category
from Item import Item

cat1 = Category("Российские автомобили")
cat2 = Category("Импортные автомобили")

item1 = Item("ВАЗ",1000,cat1)
item2 = Item("УАЗ",1500,cat1)
item3 = Item("ГАЗ",1200,cat1)

item4 = Item("BMW",5000,cat2)
item5 = Item("KIA",3000,cat2)
item6 = Item("FAW",4000,cat2)

cars = [item1,item2,item3,item4,item5,item6]

catalog = Catalog(cars)
catalog.show_items()

cart = Cart()
catalog.add_item_cart(cart)

cart.show_items()
