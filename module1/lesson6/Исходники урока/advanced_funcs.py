# Функцию можно записывать коротко через анонимную функцию:

# get_sum = lambda a,b : a + b
# print(get_sum(2,3))

# Функция map преобразует список в новый объект, который можно также преобразовать к списку

# map(function,iterable) - применяет к каждому элементу второго параметра функцию из первого параметра

# Пример 1
# numbers = [3,4,6,2]
#
# numbers = list(map(lambda item : item ** 2,numbers))
#
# print(numbers)


# Пример 2
# langs = ["PHP","JS","C#","Java"]
#
# size_langs = list(map(len,langs))
#
# print(size_langs)

# Пример

items = [["Товар 1",100],["Товар 2",300],["Товар 3",500]]

# Товар 1 стоит 100 руб.
# Товар 2 стоит 300 руб.
# Товар 3 стоит 500 руб

# print("\n".join(map(lambda item : item[0] + " стоит " + str(item[1] * 0.9),items)))


# Вместо цикла с оператором if рекомендуется использовать filter


# print(list(filter(lambda item : item[1] > 200,items)))

# Пример reduce

import functools
numbers = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x + y, numbers,100)
print("Сумма элементов списка:", product)