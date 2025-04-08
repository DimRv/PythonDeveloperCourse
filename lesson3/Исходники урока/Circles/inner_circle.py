# Пример на выход из внешнего цикла во вложенном цикле

is_check = False

while not is_check:
    print(1)
    while int(input("Введите -1 для выхода")) == -1:
        is_check = True
        break

