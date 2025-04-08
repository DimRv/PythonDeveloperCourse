"""
Проверить ученика на знание таблицы умножения.
Задаем ученику 5 рандомных примеров и получаем его
ответы. Если игрок допускает более 2 ошибок - оценка
незачет, а иначе зачет
"""

from random import randint

MAX_EX = 5

errors = 0
n = 0

while n < MAX_EX:
    x = randint(1, 9)
    y = randint(1, 9)
    result = x * y
    while 1:
        answer = input(f"Чему равно произведение {x} на {y}?\n")
        if answer.isdigit():
            answer = int(answer)
            break
        else:
            print("Не корректный ввод")
    if answer != result:
        errors += 1
    n += 1

print("-" * 40)
if errors >= 2:
    print("Не зачет")
else:
    print("Зачет")


