"""Напишите функцию get_middle(start, end), которая находит среднее
арифметическое значение в отрезке от start до end"""

from random import randint


def get_middle(start, end):
    """Получаем среднее значение от start до end"""
    return (start + end) / 2


print(get_middle(5, 10))
print(get_middle(10, 20))

