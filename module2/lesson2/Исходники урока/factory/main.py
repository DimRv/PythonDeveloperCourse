from factory.Diler import Diler
from factory.Factory import Factory
from factory.Order import Order

diler = Diler("Элвис",10)
COUNT_CARS = 20
title_models = ["Гранта","Веста","Нива","БМВ"]
factory = Factory("АвтоВаз")

order = Order(COUNT_CARS,title_models,factory)

diler.create_order(order)


# 1) При получении заказа заводом на создание некорректной модели нужно сообщить,
# что нет технической возможности изготовить данный автомобиль

# 2) Если дилер работает от 10 лет, то ему положена скидка 10% на конечный заказ
# 3) Вывести количество каждой созданной модели