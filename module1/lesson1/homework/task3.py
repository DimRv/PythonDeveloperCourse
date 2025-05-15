"""Вывести на экран текст «Silence is golden». Каждое слово должно быть на новой строке."""

print("Silence", "is", "golden", sep="\n")

inner_data = input("Введите текстовую строку:\n")
for word in inner_data.split():
    print(word)