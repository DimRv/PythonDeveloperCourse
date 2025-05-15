num_str = 1 #счечтик строк

while num_str <= 100:
    if num_str == 6:
        break
    num_field = 1 #номер столбца в текущей строке (счетчик столбцов)
    while num_field<= 10: #пока не напечатаем 10 элементов в каждой строке, цикл не остановится
        if num_field == 5:
            num_field += 1
            continue
        print(f"{num_str * num_field}\t\t",end='')
        num_field += 1
    num_str += 1 #переходим к следующей строке
    print()
