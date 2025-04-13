# Если требуется принимать произовольное количество значение в формальных параметрах,
# то используйте оператор *, который упакует все переданные значения в кортеж. Кортеж
# это статический список(неизменяемый массив)
from math import sqrt


# def sum_numbers(a,b,*args):
#     s = a + b #s = 3
#     for item in args: #item это переменная, которая по очереди принимает каждое значение из args
#         s = s + item
#     print(s)

# sum_numbers(1,2,3,4,5,7,9)


# Пример на повторение
# Пример решения квадратного уравнения

def get_discr(a,b,c):
    return b ** 2 - 4 * a * c

def get_result_solution(a,b,c):
    d = get_discr(a,b,c)
    if d > 0:
        return (-b + sqrt(d)) / 2 * a,(-b - sqrt(d)) / 2 * a
    if d == 0:
        return -b / 2 * a
    return "Нет корней уравнения"

print(get_result_solution(1,2,-3))