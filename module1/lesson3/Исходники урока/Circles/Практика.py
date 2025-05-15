# # # # # # # # from random import randint
# # # # # # # #
# # # # # # # # MAX_QUESTIONS = 5
# # # # # # # # MAX_ERRORS = 2
# # # # # # # #
# # # # # # # # errors = 0
# # # # # # # # i = 0
# # # # # # # #
# # # # # # # # while i < MAX_QUESTIONS:
# # # # # # # #     num1 = randint(1, 10)
# # # # # # # #     num2 = randint(1, 10)
# # # # # # # #     correct_answer = num1 * num2
# # # # # # # #
# # # # # # # #     q = f"Пример №{i + 1}: Сколько будет {num1} * {num2}?\n"
# # # # # # # #     user_answer = input(q)
# # # # # # # #
# # # # # # # #     if user_answer.isdigit():
# # # # # # # #         user_answer = int(user_answer)
# # # # # # # #         if user_answer == correct_answer:
# # # # # # # #             print("Верно!\n")
# # # # # # # #         else:
# # # # # # # #             print(f"Неверно. Правильный ответ: {correct_answer}\n")
# # # # # # # #             errors += 1
# # # # # # # #     else:
# # # # # # # #         print("Введите число!\n")
# # # # # # # #         continue
# # # # # # # #
# # # # # # # #     i += 1
# # # # # # # #
# # # # # # # # print(f"\nКоличество ошибок: {errors} из {MAX_QUESTIONS}")
# # # # # # # #
# # # # # # # # print("Зачет" if errors <= MAX_ERRORS else "Незачет")
# # # # # # #
# # # # # # # import random
# # # # # # #
# # # # # # # print("Реши 5 примеров:\n")
# # # # # # #
# # # # # # # attempts = 0
# # # # # # # err = 0
# # # # # # #
# # # # # # # while attempts < 5:
# # # # # # #     a = random.randint(1, 10)
# # # # # # #     b = random.randint(1, 10)
# # # # # # #     correct_answer = a * b
# # # # # # #     print(f"\nВопрос {attempts + 1}: Сколько будет {a} × {b}?")
# # # # # # #     answer = input("Ответ: ")
# # # # # # #     if answer.isdigit():
# # # # # # #         answer = int(answer)
# # # # # # #         if answer == correct_answer:
# # # # # # #             print("Правильно!")
# # # # # # #         else:
# # # # # # #             print(f"Неверно. Правильный ответ: {correct_answer}")
# # # # # # #             err += 1
# # # # # # #
# # # # # # #         attempts += 1
# # # # # # #     else:
# # # # # # #         print("Пожалуйста, введи число!")
# # # # # # #
# # # # # # # if err <= 2:
# # # # # # #     print("Зачет\n")
# # # # # # # else:
# # # # # # #     print(f"Незачет\n")
# # # # # #
# # # # # # import random
# # # # # #
# # # # # # mistakes = 2
# # # # # # ask = 5
# # # # # # grade = 'Зачёт.'
# # # # # # while ask and mistakes:
# # # # # #     a, b = random.randint(1,10), random.randint(1,10)
# # # # # #     answer = int(input(str(a) + ' * ' + str(b) + ' = '))
# # # # # #     if answer == (a*b):
# # # # # #         ask -= 1
# # # # # #         print('Верно!')
# # # # # #     else:
# # # # # #         mistakes -= 1
# # # # # #         print('Не правильно!')
# # # # # #
# # # # # # if mistakes == 0:
# # # # # #     grade = 'Незачёт.'
# # # # # # print('Ваша оценка:', grade)
# # # # #
# # # # # from random import randint
# # # # #
# # # # # answers = 10
# # # # # print("Проверка знания таблицы умножения\n")
# # # # # for i in range(10):
# # # # #     first_number = randint(1, 10)
# # # # #     second_number = randint(1, 10)
# # # # #     res = first_number * second_number
# # # # #     print(f"{first_number} * {second_number} =", end=" ")
# # # # #     math_result = int(input(""))
# # # # #     if math_result != res:
# # # # #         print(f"Ошибка! {first_number} * {second_number} = {res}")
# # # # #         answers -= 1
# # # # # print(f"Правильных ответов: {answers}")
# # # # # if 0 <= answers <= 5:
# # # # #     print("Оценка: плохо")
# # # # # if 6 <= answers <= 7:
# # # # #     print("Оценка: хорошо")
# # # # # if 8 <= answers <= 9:
# # # # #     print("Оценка: удовлетворительно")
# # # # # if answers == 10:
# # # # #     print("Оценка: отлично")
# # # #
# # # # from random import randint
# # # #
# # # # MAX_EX = 5
# # # #
# # # # errors = 0
# # # # n = 0
# # # #
# # # # while n < MAX_EX:
# # # #     x = randint(1, 9)
# # # #     y = randint(1, 9)
# # # #     result = x * y
# # # #     while 1:
# # # #         answer = input(f"Чему равно произведение {x} на {y}?\n")
# # # #         if answer.isdigit():
# # # #             answer = int(answer)
# # # #             break
# # # #         else:
# # # #             print("Не корректный ввод")
# # # #     if answer != result:
# # # #         errors += 1
# # # #     n += 1
# # # #
# # # # print("-" * 40)
# # # # if errors >= 2:
# # # #     print("Не зачет")
# # # # else:
# # # #     print("Зачет")
# # #
# # # import random as random
# # # nezach = 0
# # # count = 0
# # # while count < 5:
# # #     a = random.randint(1, 10)
# # #     b = random.randint(1, 10)
# # #     ans = int(input(f"сколько будет {a} умножить на {b}?"))
# # #     if(ans != a*b):
# # #         print(a*b)
# # #         nezach +=1
# # #     count +=1
# # #
# # # if nezach >=2:
# # #     print("Незачёт")
# # # else:
# # #     print("Зачёт")
# # from random import randint
# # i=0
# # while i<=5:
# #     i=i+1
# #     a=randint(1,9)
# #     b=randint(1, 9)
# #     err=0
# #     print("a=",a,"  b=",b)
# #     while 1:
# #        c=input("a*b=\n")
# #        if not c==a*b:
# #            err +=1
# #        if err==2:
# #            print("неверно")
# #            break
#
# i = 0 # счетчик ошибок
# count = 0
# while i <= 2 and count < 4:
#     a = randint(1, 9)
#     b = randint(1, 9)
#     answer = int(input(f'Умножьте два числа и запишите ответ: {a} * {b}\n'))
#     if answer == a * b:
#         print('Ответ верный')
#         count += 1
#     else:
#         i += 1
#         print("Вы ввели неверный ответ")
# if count == 4:
#     print('Вы справились с заданием')
# else:
#     print('Вы не справились с заданием')
MAX_ATTEMPT = 5
MAX_ERROR = 2
attempt = 1
cnt_error = 0
while attempt <= MAX_ATTEMPT:
    ex_a = randint(1,9)
    ex_b = randint(1,9)
    while 1:
        answer = input(f"Ex({attempt}): Введите ваше решение примера {ex_a} * {ex_b}\n")
        if answer.isdigit():
            answer = int(answer)
            break
    if answer != (ex_a * ex_b):
        print("Неверно")
        cnt_error += 1
    else:
        print("Верно")
    if cnt_error >= MAX_ERROR:
        break
    attempt += 1
if cnt_error < 3:
    ocenka = "ЗАЧЕТ"
else:
    ocenka = "НЕЗАЧЕТ"
print(f" Ваша оценка {ocenka}")