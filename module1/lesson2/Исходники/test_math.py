import math

# Функции это команды, которые не привязаны к объекту, то есть функции запускаем
# по имени функции

# Методы - это команды, которые привязаны к объекту. У них первым параметром всегда
# идет ссылка на объект, то есть self

# print(round(5.7653,2)) #5.77

# print(math.floor(5.7653)) #округление вниз
# print(math.ceil(5.7653)) #округление вверх
#
# fabs - получение абсолютного значения, то есть получение модуля числа.
# То есть, если передавать в fabs отрицательное число, получите положительное число

age1 = 35
age2 = 32

print(f"Разница в возрасте: {int(math.fabs(age2 - age1))}")