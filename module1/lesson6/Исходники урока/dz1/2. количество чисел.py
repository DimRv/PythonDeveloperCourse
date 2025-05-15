"""С клавиатуры вводятся N чисел. Составьте программу, которая
определяет количество отрицательных, количество положительных
и количество нулей среди введенных чисел. Значение N вводится с
клавиатуры. При вводе нечислового значения вывести сообщение
об ошибке и просим ввести повторно именно числовое значение.
Используйте цикл for"""



def get_count(N):
    count_positive = count_negative = count_zero = 0
    for _ in range(N):
        num = input("Введите число: ")
        if num.lstrip('-+').isdigit():
            num = int(num)
            if num > 0:
                count_positive += 1
            elif num < 0:
                count_negative += 1
            elif num==0:
                count_zero += 1
        else:
            print('Ошибка! Просьба ввести числовое значение')
    return f"\tКоличество положительных чисел: {count_positive}\n\
    Количество отрицательных чисел: {count_negative}\n\
    Количество введеных нулей: {count_zero}"


def count_num(N):
    #без for, не засчитывает нечисловые значения
    count_positive = count_negative = count_zero = 0
    while N>0:
        num = input("Введите число: ")
        if num.lstrip('-+').isdigit():
            N-=1
            num =int(num)
            if num>0:
                count_positive += 1
            elif num<0:
                count_negative += 1
            elif num==0:
                count_zero += 1
        else:
            print('Ошибка! Просьба ввести числовое значение')
    return f"\tКоличество положительных чисел: {count_positive}\n\
    Количество отрицательных чисел: {count_negative}\n\
    Количество введеных нулей: {count_zero}"

N = int(input("Введите, какое количество значений будет использовано? "))
print(get_count(N))

