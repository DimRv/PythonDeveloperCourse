"""Вывести все простые числа от 2 до 100"""


MAX_N = 100
n = 2
print(f"Простые числа в диапазоне от {n} до {MAX_N}:")

while n < MAX_N:
    a = 2
    max_a = n // 2
    while a <= max_a:
        if n % a == 0:
           break
        a += 1
    else:
        print(f"{n} ", end="")
    n += 1
