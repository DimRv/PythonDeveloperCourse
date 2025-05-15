"""Напечатать таблицу умножения от 2 до 5:"""

print("1. Напечатать таблицу умножения от 2 до 5")

num_str_min = 2                                         # счётчик строк
num_str_max = 9                                         # максимальное количество строк
while num_str_min <= num_str_max:                       # цикл с условием

    num_field_min = 2                                   # счётчик столбцов - номер столбца в строке
    num_field_max = 5                                   # максимальное количество столбцов

    while num_field_min <= num_field_max:               # цикл с условием
        print(f"{num_field_min} * {num_str_min} = {num_str_min * num_field_min}\t\t",end='')

        num_field_min += 1                              # столбец добавляем +1
    num_str_min += 1                                    # строку добавляем +1
    print()                                             # print() пустой - для перехода на новую строку