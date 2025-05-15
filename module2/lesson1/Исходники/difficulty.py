def find_max(my_list):
    """Пример сложности O(N)"""
    item_max = my_list[0] #O(1)
    for i in range(1,len(my_list)): #O(N - 1)
        if my_list[i] > item_max:#O(1)
            item_max = my_list[i]#O(1)
    return item_max#O(1)

# O(1 + N - 1 + 1) = O(N)


def has_dublicates(my_list):
    """Поиск дубликатов в списке"""
    for i in range(len(my_list)): #O(N)
        for j in range(len(my_list)):  #O(N)
            if i != j:#O(1)
                if my_list[i] == my_list[j]:#O(1)
                    return True#O(1)
    return False#O(1)

# O(N ^ 2)