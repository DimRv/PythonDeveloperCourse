from random import randint


def get_salaries(n):
    s = ""
    for i in range(n):
        s += str(randint(50000,200000)) + "\n"
    return s

print(get_salaries(10))