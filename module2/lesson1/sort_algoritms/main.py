"""
Алгоритмы сортировки и их разбор:

 - сортировка выбором
 - пузырьковая сортировка
 - сортировка вставками
 - сортировка слиянием (принцип разделяй и властвуй)
 - быстрая сортировка (принцип разделяй и властвуй)

 В Python по умолчанию Timsort - объединение сортировки вставками и сортировки слиянием.
 Сортировка вставкой используется если список меньше 64 элементов
 Иначе:
•TimSort делит входной массив на подмассивы;
•Сортирует подмассивы вставками;
•Объединяет их попарно сортировкой слиянием;
•И возвращает отсортированный массив.
 """


def swap(arr, a, b):
    """Перестановка элементов a и b в массиве"""
    arr[a], arr[b] = arr[b], arr[a]
    print('swap', arr)


def selection_sort(unsorted):
    """Сортировка выбором - сравниваются i и j значения"""
    n = len(unsorted)  # O(1)
    for i in range(0, n):  # O(N)
        current_min = unsorted[i]  # O(1)
        min_index = i  # O(1)
        for j in range(i, n):  # O(N)
            if unsorted[j] < current_min:  # O(1)
                current_min = unsorted[j]  # O(1)
                min_index = j  # O(1)
        # меняем i-тое и j-тое значения
        swap(unsorted, i, min_index)  # O(1)
# O(N) * O(N) = O(N^2)


arr = [12, 3, 7, 5, 1]
print(arr)
selection_sort(arr)
print('-'*40)


def bubble_sort(unsorted):
    """Сортировка пузырьком - сравниваются соседние элементы"""
    n = len(unsorted)
    for i in range(0, n - 1):  # O(N)
        # флаг нужен для быстрого завершения если нет перестановки
        swapped = False
        for j in range(0, n - 1 - i):  # O(N)
            if unsorted[j] > unsorted[j + 1]:
                swap(unsorted, j, j + 1)
                swapped = True
        if not swapped:
            return
# O(N) * O(N) = O(N^2)


arr = [12, 3, 7, 5, 1]
print(arr)
bubble_sort(arr)
print('-'*40)


def insertion_sort(unsorted):
    """ сортировка вставками - сравнение с предыдущими элементами"""
    n = len(unsorted)
    for i in range(1, n):
        # запоминаем значение элемента и индекс
        val = unsorted[i]
        pos = i
        # проходим по массиву в обратную сторону, пока не найдём элемент больше текущего
        while pos > 0 and unsorted[pos - 1] > val:
            # переставляем элементы местами , чтобы получить правильную позицию
            unsorted[pos] = unsorted[pos - 1]
            print(unsorted, pos, f'({val})')
            pos -= 1
        unsorted[pos] = val
        print(unsorted)


arr = [12, 3, 7, 5, 1]
print(arr)
insertion_sort(arr)
print('-'*40)


def divide(unsorted, lower, upper):
    """ рекурсивная функция для разделения массива на два подмассива для сортировки """
    print(unsorted, lower, upper)
    # с помощью рекурсии достигнут базовый случай
    if upper <= lower:
        return
    mid = (lower + upper) // 2
    divide(unsorted, lower, mid)
    divide(unsorted, mid + 1, upper)
    merge(unsorted, lower, mid, mid + 1, upper)


def merge(unsorted, l_lower, l_upper, r_lower, r_upper):
    """ объединение двух сортированных массивов в один """
    print(unsorted, l_lower, l_upper, r_lower, r_upper)
    i, j = l_lower, r_lower
    temp = []
    print('start_temp', temp)

    # проходим по индексам
    while i <= l_upper and j <= r_upper:

        # определяем, какое значение следующим вставить во временный массив
        if unsorted[i] <= unsorted[j]:
            temp.append(unsorted[i])
            i += 1
        else:
            temp.append(unsorted[j])
            j += 1

    # одно из условий выше заканчивается первым
    # поэтому обрабатываем незаконченный случай
    while i <= l_upper:
        temp.append(unsorted[i])
        i += 1
    while j <= r_upper:
        temp.append(unsorted[j])
        j += 1
    print('end_temp',temp)
    # присваиваем значения из временного массива
    for y, k in enumerate(range(l_lower, r_upper + 1)):
        unsorted[k] = temp[y]
        print(unsorted)


arr = [12, 3, 7, 5, 1]
print(arr)
divide(arr, 0, 4)
print('-'*40)


def quick_sort(unsorted, start, end):
    """ быстрая сортировка
    пивот - точка опоры, такой индекс при котором значения слева всегда меньше, а справа больше
    """
    print(unsorted, start, end)
    # останавливаемся, когда индекс слева достиг или превысил индекс справа
    if start >= end:
        return
    # определяем позицию следующего пивота
    i_pivot = partition(unsorted, start, end - 1)
    # рекурсивный вызов левой части
    quick_sort(unsorted, start, i_pivot)

    # рекурсивный вызов правой части
    quick_sort(unsorted, i_pivot + 1, end)


def partition(unsorted, start, end):
    """ arrange (left array < pivot) and (right array > pivot) """

    # выбираем значение pivot как последний элемент неотсортированного сегмента
    pivot = unsorted[end]

    # назначаем на pivot значение левого индекса
    i_pivot = start

    # проходим от начала до конца текущего сегмента
    for i in range(start, end):

        # сравниваем текущее значение со значением pivot
        if unsorted[i] <= pivot:

            # меняем местами текущее значение и значенрие pivot
            swap(unsorted, i, i_pivot)
            print('if', unsorted)

            # увеличиваем значение пивота
            i_pivot += 1

    # ставим пивот в правильную позицию, заменив со значением слева
    swap(unsorted, i_pivot, end)
    print("f", unsorted)

    # возвращаем следующее значение пивота
    return i_pivot

# O(N*log(N))

arr = [12, 3, 7, 5, 1]
print(arr)
quick_sort(arr, 0, 5)
print('-'*40)