# a = (1,2,3)
# a[0] = 5
# print(a[0])
# Преобразование списка к кортежу
# my_tuple = tuple([1,2,3,4])
# print(type(my_tuple))

# Пример
# Найти сумму всех элементов кортежа в котором в качестве значений могут быть списки

my_tuple = [1,2,3,(10,20,30),5]

# print(sum(my_tuple[3])) #60

# print(my_tuple[3][2])

# result = 0
#
# for item in my_tuple:
#     if isinstance(item,tuple):
#        # for i in item:
#        #     result += i
#         result += sum(item)
#     else:
#         result += item
# print(result)

# x = (3,2,1)
# print(sorted(x))

# test_tuple = 1,
# print(type(test_tuple))