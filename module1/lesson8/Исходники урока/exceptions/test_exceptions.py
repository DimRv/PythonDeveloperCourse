# Сущетсвуют разные виды ошибок - синтаксические и ошибки в рантайме, то есть
# в момент запуска программы. Ошибки в рантайме можно обрабатывать с помощью спец.
# операторов. Инструкции, в которых возможна ошибка в момента запуска нужно обернуть
# в оператор try. Если возникает ошибка, то немедленно из блока try переходим в блок
# except и в нем обрабатываем ошибку. Такие действия предотвращают завершение работы
# нашего скрипта ошибкой.

# Пример 1

from random import randint

# a = 10
# b = randint(0,2)
#
# try:
#     print(f"{a} / {b} = {a / b}")
#     print(111)
# except ZeroDivisionError as e:
#     print(e.__str__())
# print("Данная инструкция не выполнится если b = 0")

# Пример 2

# while 1:
#     a = input("Введите число")
#     if a == 'q':
#         break
#     b = input("Введите число")
#     if b == 'q':
#         break
#     try:
#         res = int(a) / int(b)
#         print(f"{a} / {b} = {res}")
#     except ZeroDivisionError:
#         print("На 0 делить нельзя!")
#     except ValueError:
#         print("Вы ввели некорректное значение!")
#     except:
#         print("Возникла непредвиденная ошибка")

# Пример 3

# my_file = 'test.txt'
#
# try:
#     x = 1
#     with open(my_file,"r") as file:
#         print(file.readlines())
# except FileNotFoundError:
#     print("Файл не найден")
#
# print(x)

# Пример 4
# Оператор finally содержит блок инструкций, которые обрабатываются независимо от
# того была ошибка или ее не было. Оператор используется всегда для закрытия ресурсов

file = None

try:
    file = open('test.txt', 'w')
    # content = file.readlines()
except FileNotFoundError:
    print("Файл не существует")
finally:
    print("Этот блок выполняется даже если будет ошибка в try")
    if file:
        file.close()
        print("Ресурсы освобождены")
    else:
        print("Файл не был создан!")