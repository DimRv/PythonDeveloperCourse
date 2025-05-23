"""2.   Вывести все простые числа от 2 до 100"""
print("2.   Вывести все простые числа от 2 до 100")
from math import sqrt

i = 2                             # счётчик чисел, по совпадению может стать простым числом
i_max = 100                       # необходимое число, до которого необходимо найти простые числа
while i <= i_max:                 # цикл с условием, диапазон, в котором ищем простые числа
    is_simple = True              # условно считаем, что проверяемое число - простое


    x = 2                              # х число, должно быть всегда меньше в 2 раза или равно проверяемому числу...

    # while x <= sqrt(i) or x <= i / 2:   # 1v цикл с условием, число x должно соответствовать условию
    # while x <= sqrt(i) and x <= i / 2:  # 2v
    # while x <= i / 2:                   # 3v

    while x <= sqrt(i):                   # 4v
        if i % x == 0:            # если проверяемое число делится без остатка, то значит проверяемое число - не простое, а составное
            is_simple = False     # значит, проверяемое число i - не простое
            break                 # выход из цикла сразу делаем, чтоб проверять другие числа i+1 на "простоту"
        x += 1                    # если break не случился, нужно i на "простоту" проверить в цикле другим числом, большим на 1

    if (is_simple):               # Если true
        print(f"{i}",end="   ")    # вывод простых чисел
    i += 1                         # счётчик чисел увеличиваем, это новое число будем проверять на "простоту"

#=============================================================================================
#=============================================================================================
# черновик
        # print(f"{str(i)}", end=", ")  # вывод простых чисел
# =============================================================================================
        # print(f"{i}", end=" " if {i == 97} else f"{i}", end=", ")  # вывод простых чисел
# =============================================================================================
#         simple1 = str(i)
#         print(f"{simple1}", end=",  ".rstrip(","))
#     i += 1
