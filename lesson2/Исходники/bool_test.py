# current_year = input("Введите текущий год\n")
from random import randint

# print(id(current_year) == id("2025"))

number_day = int(input("Введите день недели от 1 до 7"))
is_work_day = number_day > 0 and number_day < 6

is_weekend = number_day == 6 or number_day != 7

print(f"День №{number_day} - это будний день? Ответ: {is_work_day}")
print(f"День №{number_day} - это выходной день? Ответ: {is_weekend}")
