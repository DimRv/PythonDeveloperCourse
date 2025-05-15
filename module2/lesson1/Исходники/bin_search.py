def bin_search(items,find_item):
    #Отсортируем коллекцию
    items.sort()
    print(items)
    #индекс начала поиска
    i = 0
    # индекс последнего элемента
    j = len(items) - 1
    # Индекс центрального элемента
    m = j // 2

    while items[m] != find_item and i <= j:
            if find_item > items[m]:
                i = m + 1
            else:
                j = m - 1
            m = int((i + j) / 2)
    if i > j:
        print("Элемент не найден")
        return -1
    # Вернем индекс найденного элемента
    return m

print(bin_search([5,3,1,8,6],50))