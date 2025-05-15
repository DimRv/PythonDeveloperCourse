"""Сортировка словаря по ключу и значению"""

my_dict = {'c':10,'a':5,'b':2}

# Для сортировки словаря используйте функцию sorted. У этой функции первый параметр
# это элементы нашего словаря, а второй параметр это лямбда выражение
# в котором явно указываем как сортировать словарь. Шаблон для сортировки:

# key = lambda item : item[0]
# Если в [] стоит 0 значит сортируем по ключу, а если 1, то по значению


dict_sort_by_key = dict(sorted(my_dict.items(),key=lambda item:item[0]))
dict_sort_by_value = dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(dict_sort_by_value)