from random import randint

# Пример 1

# def show_sum():
#     s = 0
#     while 1:
#         x = randint(1,9)
#         print(x)
#         s += x
#         if input("Завершить работу цикла? (Y/N)") == "Y":
#             print(s)
#             return 1,2
# show_sum()

# Пример 2

# def func(a):
#     return 10,20,(1,2,3),30
# print(func()[2][1])


# Пример 3

# Вложенные функции. Есть возможность делать функцию внутри другой функции.
# Вложенные функции знают всё о внешней функции, а внешняя функция имеет лишь
# возможность вызывать вложенные функции. То есть переменные вложенной функции
# не видны во внешней функции

# def pc(title,size_ram,size_hard,is_on = False):
#     def ram(size):
#         info = "модуль RAM запущен" if is_on else "модуль RAM выключен"
#         print(f"ПК {title} имеет размер RAM: {size}\n{info}")
#     def hard(size):
#         info = "Жесткий диск запущен" if is_on else "Жесткий диск выключен"
#         print(f"ПК {title} имеет объем жесткого диска: {size}\n{info}")
#
#     ram(size_ram)
#     hard(size_hard)
#
#     return ram,hard

# pc("ACER")[0](1024)

# pc("ACER",8,1024,False)

# Пример 3.2

def calc(action,b,c):
    print(action(b,c))
def sum(a,b):
    return a + b
def dif(a,b):
    return a - b

calc(sum,2,3)

# Пример 3.2

# def get_sum(a,b):
#     return a + b
# Можно функцию присвоить переменной и переменная сама станет функцией
# test = get_sum
# print(test(2,3))

# Пример 4 (Замыкания)

def outer(a):
    def sum(b):
        return a + b
    return sum

# Цель замыкания - генерация новых функций

# sum_three = outer(3)
# print(sum_three(1))
# print(sum_three(2))
# print(sum_three(3))
#
#
# sum_ten = outer(10)
# print(sum_ten(1))
# print(sum_ten(2))
# print(sum_ten(3))