from random import randint

MIN_MONEY = 5000 #минимальная сумма для начала игры
COUNT_TRY = 3 #количество попыток угадать число
COUNT_TIME = 0
money = int(input('Введите сумму'))
while money > MIN_MONEY:
    while True: #в цикле сможем гарантированно получить корректную ставку
        rate = input("Введите Вашу ставку")
        if rate.isdigit():
            rate = int(rate)
            if rate <= money:
                print("Ставка принимается")
                break
            else:
                print("Ставка не может превышать Вашу сумму! Введите снова")
    number = randint(1,10)
    print(number) #для теста выводим загаданное число
    count = 0 #счетчик попыток

    while count < COUNT_TRY:
        answer = input(f"Введите число. Попытка №{count + 1}. (Для выхода введите СТОП)\n")
        if answer.upper == "СТОП":
            break
        if int(answer) == number:
            money += rate
            print(f"Вы угадали! Ваша сумма = {money}")
            break
        else:
            count += 1
            if count == COUNT_TRY:
                print(f"Вы проиграли! Ваша сумма = {money} Было загадано: {number}")
                money -= rate
    COUNT_TIME += 1
    if input('Вы желаете сыграть еще раз? (y/n)').lower() != 'y':
        print(f"Игра завершена. Было сыграно: {COUNT_TIME} партий")
        break

