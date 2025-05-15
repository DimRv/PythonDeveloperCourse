# test_set = set() #создали пустое множество
# while 1:
#     answer = input('Введите значение для добавления во множество или -1 для выхода\n')
#     if answer == "-1":
#         break
#     test_set.add(answer)
#
# print(test_set)

# Специальные методы для множеств

# a = {1,2,3}
# b = {4,2,5}
# # c = a.union(b) #{1, 2, 3, 4, 5}
# # c = a.intersection(b) #получим общие элементы, это 2 в нашем примере
# c = a.difference(b)#{1,3}
# print(c)

numbers = [2,3,4,5,2]
numbers = list(set(numbers)) #избавляемся в списке от дубликатов
print(numbers)