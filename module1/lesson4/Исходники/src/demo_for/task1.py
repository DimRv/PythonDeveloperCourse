"""
Присвойте переменной с именем total значение 0.
Предложите пользователю ввести пять чисел, и после каждого ввода спрашивайте,
 хочет ли он включить это число в суммирование. Если ответ будет положительным,
  прибавьте введенное число к total. Если же ответ будет отрицательным, число к total
   не прибавляется. После ввода всех пяти чисел выведите значение total.

"""

total = 0
for _ in range(5):
    while 1:
        num = input("Введите положительное число\n")
        if not num.isdigit():
            print("Вы ввели некорректное значение")
            continue
        num = int(num)
        break
    if input("Учесть введенное значение в суммировании? (y/n)").upper() == 'Y':
        total += num
print(total)

