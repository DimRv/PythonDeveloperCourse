"""Написать программу определения стоимости разговора по телефону с учетом
скидки 20%, предоставляемой по субботам и воскресеньям"""

from random import randint

price = randint(1, 3) * 1000
print(f"Стоимость разговора а по будням: {price}руб. На выходных действует скидка 20%.")

day_number = randint(0, 6)
if day_number >= 5:
    price *= 0.8

day_names = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресение"]

print(f"Сегодня {day_names[day_number]}. Стоимость разговора составит: {int(price)}руб.")


