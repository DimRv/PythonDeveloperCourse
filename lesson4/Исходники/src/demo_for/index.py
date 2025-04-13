# Функция range - генерирует набор чисел

# print(list(range(1,10)))

# range(n) - генерирует числа от 0 до n
# range(a,b) - генерирует числа от a до b
# range(a,b,step) - генерирует числа от a до b с шагом step

# print(list(range(1,10,3)))#[1, 4, 7]

# Конструкция цикла for

# for item in множество элементов:
#     тело цикла

# Пример 1

# Вывести все четные числа от 1 до 10

#
# for i in range(2,10,2):
#     print(i)

# print(list(range(10)))

# Пример 2

# for i in range(10):
#     if i <= 8:
#         continue
#     print(i)

# Пример 3 (for/else)

for i in range(10):
   test = input("Введите что-нибудь")
   break
else:
    print("Условие в цикле не разу не выполнилось")