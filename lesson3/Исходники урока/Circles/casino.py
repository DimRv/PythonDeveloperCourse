"""Игра Казино - игрок может приступить к игре, если его сумма от 10_000.
В этом случае ему дается 3 попытки, чтобы игрок угадал случайное число от 1 по 9.
Игрок должен сделать ставку, что угадает за 3 попытки. Если он сможет угадать,
то к его исходной сумме прибавляем его ставку. А если не угадает, то ставку вычитаем
из его суммы и выводим какое число было загадано
"""
from random import randint


MIN_MONEY = 10_000 #Сумма при которой допускается игрок
MIN_RATE = 1000 #Минимальная ставка
MAX_TRY = 3 #макс. количество попыток

money = int(input("Введите Вашу сумму\n"))
if money < MIN_MONEY:
    print("Средств недостаточно для начала игры")
else:
    while 1: #создали бесконечный цикл, чтобы заставить игрока ввести корректную ставку
        rate = input('Сделайте Вашу ставку')
        if rate.isdigit() and MIN_RATE <= int(rate) <= money:
            print("Ставка принимается! Игра началась!")
            rate = int(rate)
            break
        print("Вы ввели некорректную ставку!")

    number = randint(1,9) #это число нужно будет угадать за 3 попытки
    answers = [] #список введенных ответов, чтобы если не угадает покать его ответы
    i = 0 #счетчик попыток
    while i < MAX_TRY:
        answer = int(input(f"Попытка №{i + 1}:\n"))
        if answer == number:
            money += rate
            print(f"Вы угадали! Ваша сумма =",money)
            break
        else:
            answers.append(answer)
            if i == MAX_TRY - 1:
                money -= rate
                print(f"Вы проиграли! Ваша сумма =", money,",n =",number,"\nВы "
                                                                         "вводили",answers)
        i += 1

