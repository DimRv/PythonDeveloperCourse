a = 1
b = 2


def is_even(a):
    return a % 2 == 0


def calc(a,b):
    if is_even(a) and is_even(b):
        return True
    return False

calc(a,b)