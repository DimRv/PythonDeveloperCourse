"""2) Вывести в консоль исходную матрицу из файла и
вывести в консоль матрицу из файла таким образом,
чтобы каждая строка была возведена в степень
равную номеру строки"""

with open('martix.txt', 'w') as f:
    f.write("1 2 3\n4 5 6\n7 8 9")

with open('martix.txt', 'r') as f:
    file = f.read()
print(f"Исходный {f.name}:\n{file}")

file_lines = file.split("\n")
n = 0
result = ''
for line in file_lines:
    n += 1
    new_numbers = [str(int(number) ** n) for number in line.split()]
    result += ' '.join(new_numbers) + "\n"
print(f"Обновленный:\n{result}")



