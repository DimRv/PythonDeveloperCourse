# Функция это блок кода, который можно запустить из любого места в программе

# Пример 1
# def show_sum(a = 0,b = 1):
#     print(a + b)
#
# show_sum(b = 5)

# Пример 2 (локальные и внешние переменные)

# outer = 10
#
# def show_sum(a,b):
#     outer = 1
#     s = a + b + outer
#     print(s)
#
# show_sum(2,3) #6
# print(outer)

# Пример 3 (global)

# outer = 10
#
# def show_sum(a,b):
#     global outer
#     outer = 1
#     s = a + b + outer
#     print(s)
#
# show_sum(2,3) #6
# print(outer)

# Пример 3 (global)

# outer = 10
#
# def show_sum(a,b):
#     global outer
#     outer = 3
#     s = a + b + outer
#     print(s)
#
# show_sum(2,3) #6
# print(outer)

# Пример 4 (типизированные параметры)

# def show_sum(a:int,b:int):
#     print(a + b)
#
# show_sum("2","3") #23

# Пример 5(Возврат значения)

# У функции по умолчанию нет результата, то есть он равен None
# Оператор return это оператор, который присваивает функции значение и завершает
# функцию. Оператор return это аналог break для цикла.

# def show_sum(a:int,b:int)->str:
#    return a + b
#
# res = 2 * show_sum("3","5")
#
# print(res)

# Пример 6 (оператор return v2)

def calc(a,b):
   if is_even(a) and is_even(b):
      return a + b
   return a * b

def is_even(n):
   """Проверка на четность"""
   return n % 2 == 0

print(calc(2,8))


