"""
С клавиатуры вводятся N чисел. Составьте программу, которая
определяет количество отрицательных, количество положительных
и количество нулей среди введенных чисел. Значение N вводится с
клавиатуры. При вводе нечислового значения вывести сообщение
об ошибке и просим ввести повторно именно числовое значение.
Используйте цикл for.
"""


def is_number(value: str) -> bool:
    """Проверка является ли значение переданное в параметре числом"""
    value = value[1:] if value.startswith("-") else value
    return value.isdigit()


N = 5
count_negative = count_positive = count_null = 0
for _ in range(N):
    while 1:
        num = input("Введите число:\t")
        if is_number(num):
            num = int(num)
            break
        else:
            print("Вы ввели не число.")
    if num > 0:
        count_positive += 1
    elif num < 0:
        count_negative += 1
    else:
        count_null += 1


print(f"Вы ввели числа:\n\tположительные: {count_positive}\n\tнули: {count_null}\n\tотрицательные: {count_negative}")
