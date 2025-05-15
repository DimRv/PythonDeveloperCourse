'''Напишите функцию get_middle(start, end),
которая находит среднее арифметическое значение
в отрезке от start до end'''

def average(start,end):
    #нашла формулу в интернете
    count = end - start + 1
    sum_num= (start+end)*count/2
    return sum_num/count


def average_hand(start,end):
    #посчитать вручную, без формулы
    sum_num = count = 0
    for i in range (start, end+1):
        sum_num += i
        count += 1
    return sum_num/count


def get_middle(start,end):
    start, end = int(start), int(end)
    if start > end:
        start, end = end, start
    return average_hand(start, end)




start = input("Введите начало отрезка: ")
end = input("Введите конец отрезка: ")

print(get_middle(start,end))