# Модуль - это файл, в котором могут храниться, функции, классы, объекты
# Для импорта модулей существует два способа:
# 1) import название модуля
# При таком импорта функции модуля доступны только при обращении к ним через имя модуля,
# то есть math.sqrt()

# 2) Можно явно указывать какие функции из модуля мы импортируем
from math import sqrt,pow,pi
# В этом случае при вызове функций из модуля не указываем имя модуля

# print(int(sqrt(9)))
# print(pi)

# print(pow(8,1/3))

# Найти максимальное значение из набора чисел можно через max(любое количество цифр через запятую)

# print(min(2,5,1))


# Задание - вывести числа по возрастанию от минимального к максимальному
a = 49
b = 50
c = 1

max_var = max(a,b,c) #5
min_var = min(a,b,c) #1
middle = a + b + c - max_var - min_var

print(min_var,middle,max_var)
