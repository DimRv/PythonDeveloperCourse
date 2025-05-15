# Пример 1
from random import randint

items = [1,2,3,4,5,6,7,8]


# print(items[::3])


# Пример 2
# Построить 1 список, содержащий 5 повторов значений 123

# list = [1,2,3] * 5
# print(list)

# Пример 3
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
# print(id(list1))
# list2 = list(range(1,6))
# print(id(list2))

# print(list1 is list2)

# print(list1)
# print(list2)

# Пример 4

# numbers = [randint(1,9) for i in range(10)]
# print(numbers)
#
# numbers = [item + 10 for item in numbers if item % 2 == 0]
# print(numbers)

# Пример 5 (метод для сортировки)
# numbers = [randint(1,9) for i in range(10)]
# print(numbers)
# 1ый способ:
# numbers.sort() #сортировка по возрастанию
# numbers.sort(reverse=True)#сортировка по убыванию
# print(numbers)

# 2ой способ
# numbers = sorted(numbers)
# print(sorted(numbers,reverse=True)) #сортируем по убыванию
# print(numbers)

# Пример 6
langs = [item.upper() for item in ['java','python','js','c#']]
# print(langs)
# Способы поиска подстроки в строке совпадают со способами поиска в списке
# print("Элемент найден"
#       if input("Введите искомый элемент\n").upper() in langs
#       else "не найден")

# Получение индекса элемента
# Метод index можно использовать только для гарантированно существующих элементов
# find = "JS"
# if langs.__contains__(find):
#     print(langs.index(find))

# Метод count вернет количество элементов на основе параметра

# numbers = [randint(1,9) for i in range(10)]
# print(numbers)

# print(numbers.count(int(input("Введите значение для поиска"))))

# Пример 7 (добавление элемента)
# append(value) - добавить элемент в конец списка
# insert(index,value) - добавить новый элемент в позицию, указанную в первом аргументе
# numbers.append(10)
# numbers.insert(0,10)
# print(numbers)

# Пример 8 (Удаление элементов)
# Метод pop удаляет элемент и его возвращает
# 1) pop() - удаление последнего элемента
# 2) pop(index) - удаление элемента по индексу
# 3) remove(value) - не возвращает удаляемый элемент

# print(f"Вы удалили {numbers.pop(0)} элемент")
# remove требует обязательное наличие удаляемого элемента!
# numbers.remove(1) #удаляем первую найденную единицу
# print(numbers)

# Пример 9
# Удаление списка
numbers = [randint(1,9) for i in range(10)]
print(numbers)
# del numbers #удаляем список
numbers.clear() #очистили список от значений

print(numbers)