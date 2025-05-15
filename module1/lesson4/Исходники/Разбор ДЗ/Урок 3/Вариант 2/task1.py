"""Напечатать таблицу умножения от 2 до 5"""


MAX_X = 9
MAX_Y = 5

x = 2

while x <= MAX_X:
    y = 2
    while y <= MAX_Y:
        print(f"{y} x {x} = {x * y}\t\t", end="")
        y += 1
    print()
    x += 1
