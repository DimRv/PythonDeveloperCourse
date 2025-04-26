from openpyxl import  Workbook

# Создаем новую книгу в Excel

book = Workbook()

#Получаем активный лист
page = book.active

# Записываем в ячейки данные

page['A1'] = "Audi"
page['B1'] = 1000

page['A2'] = "BMW"
page['B2'] = 1200

book.save("cars.xlsx")