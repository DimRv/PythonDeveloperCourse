"""
Создать программу на Python для решения квадратного уравнения.
"""

import re


def get_values():
    while 1:
        inner_data = input("Введите коэффициенты квадратного уравнение a b c через пробел:\n")
        values = []
        for inner_value in inner_data.split():
            if inner_value.lstrip('-').isdigit():
                values.append(int(inner_value))
            elif re.match(r'\d+\.\d+', inner_value.lstrip('-')):
                values.append(float(inner_value))
            else:
                print(f"Вы введи не корректные данные")
        if len(values) == 3:
            break
    return values


a, b, c = get_values()
if a == 0:
    print("Это не квадратное уравнение")
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        result = (-b - discriminant ** .5) / 2 * a, (-b + discriminant ** .5) / 2
        print(f"Уравнение имеет два корня: %.5f и %.5f" % (round(result[0], 5), round(result[1], 5)))
    elif discriminant == 0:
        result = -b / 2 * a
        print(f"Уравнение имеет один корень: %.5f" % result)
    else:
        print("Уравнение не имеет корней")





