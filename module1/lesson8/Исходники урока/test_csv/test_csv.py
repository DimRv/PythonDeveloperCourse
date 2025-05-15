import csv

persons = [
    {"fio":"Иванов Иван Иванович","position":"Программист","salary":200_000},
    {"fio":"Петров Иван Иванович","position":"DevOps","salary":250_000},
    {"fio":"Сидоров Иван Иванович","position":"Аналитика","salary":120_000},
]

# Запись в файл
# with open('persons.csv','w',newline='',encoding='utf-8') as file:
#     columns = ['fio','position','salary']
#     obj = csv.DictWriter(file,fieldnames=columns)
#     obj.writeheader()
#     obj.writerows(persons)

# Чтение из файла
with open('persons.csv', 'r', newline='', encoding='utf-8') as file:
    obj = csv.DictReader(file)
    for item in obj:
        print(f"{item['fio']} работает в должности {item['position']}")


