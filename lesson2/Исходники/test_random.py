"""В этом скрипте рассматриваются функции модуля random"""
from asyncio.base_futures import isfuture
from random import *

# Для получения рандомных чисел используйте функции

# 1) randint(a,b) - получение случайного целого числа в отрезке [a,b]
# 2) random() - получение случайного вещественного числа в отрезке [0,1)
# 3) randrange(a,b,step)

# print(randrange(1,10,3)) #случайные числа от 1 до 10. Эта функция
# гарантирует, что следующее значение будет либо таким же, либо на шаг меньше, либо на
# В примере выше возможны варианты чисел: 1, 4, 7

# print(randint(1,10))

# print(random())

# Для получения через random() случайное вещественное число в отрезке [a,b) - используйте
# формулу:

# random() * (b - a) + a
# [10,10]
# print(random() * (10 - 1) + 1)  [1,10)

# [7,20)

# random() * 14 + 7



# [-10,10]

# random() * (11 + 10) - 10)

# print(random() * 20 - 10)


age1,age2,age3 = randint(20,50),randint(20,50),randint(20,50)

# max_age = max(age1,age2,age3)
# min_age = min(age1,age2,age3)
# middle = age1 + age2 + age3 - min_age - max_age
# print(max_age,middle,min_age)

# Универсальный способ решения для любого количества значений
# ages = [age1,age2,age3]
# ages.sort(reverse=True)  #reverse=True - означает, что сортировка по убыванию
# print(ages)