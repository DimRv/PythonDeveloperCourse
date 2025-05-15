# Проверим ответ юзера на корректное значение

while 1:
    answer = input("Введите значение от 1 до 10")
    if not answer.isdigit():
        print("Вы ввели не число!")
        continue
    if 1 <= int(answer) <= 10:
        print("Принимается")
        break
    else:
        print("Вы ошиблись с отрезком допустимых значений")
