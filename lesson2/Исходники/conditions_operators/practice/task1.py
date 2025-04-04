# """
# Создать случайную стоимость покупки от 100руб до 2000руб. Если стоимость покупки
# более 500р, то скидка 5%, а если стоимость покупки от 1000р, то скидка 10%.
# Вывести стоимость покупки с учетом скидки.
# """
#
#
# Дмитрий
# 21:29
#
# from random import randint
#
# price = randint(100, 2000)
# print(f"start price: {price}")
# if price >= 1000:
#     price *= 0.9
# elif price >= 500:
#     price *= 0.95
#
# print(f"end price: {price}")
# Мария П.
# 21:29
#
# import random
# purchase = random.randint(100, 2000)
#
# disc_percent = 0
# if purchase >= 1000:
#     disc_percent = 10
# elif purchase > 500:
#     disc_percent = 5
#
#
# discount = purchase * disc_percent / 100 #размер скидки
# f_cost = purchase - discount
# print(f"Стоимость с учетом скидки: {f_cost} руб.")
# Орлов Константин
# 21:29
#
# from random import *
#
# price = round(random() * (2000 - 100) + 100, 2)
# print(f'random price {price}')
#
# if 500 < price < 1000:
#     price *= 0.95
#     print('Discount 5%')
# elif price > 1000:
#     price *= 0.9
#     print('Discount 10%')
#
# print(round(price, 2))
# Иван Добровольский
# 21:29
#
# from random import
#
# price_ = random.randint(100, 2000)
# price_ = float(price_)
#
# if 500 < price_ < 1000:
#     price_ *= 0.95
# elif 1000 < price_:
#     price *= 0.9
# Константин Борцов
# 21:29
#
# from random import *
# price=randint(100,2000)
# print(price)
# if 500<price<=1000:
#     discount=5
# elif price>=1000:
#     discount=10
# else:
#     discount=0
# print(price*(1-discount/100))
# Иван Кукса
# 21:30
#
# import random
#
# price = random.randrange(100, 2000)
#
# discount = 0
#
# if price > 500:
#     discount = 5
# elif price > 1000:
#     discount = 10
#
# print(f"Стоимость с учетом скидки {price / 100 * (100 - discount)}")
