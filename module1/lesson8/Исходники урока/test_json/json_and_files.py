import json
from pprint import pprint

# Пример записи словаря в json

shop = {}
shop["cars"] = []
shop["cars"].append({
    "title":"Audi",
    "price":1000
})
shop["cars"].append({
    "title":"BMW",
    "price":1200
})
shop["cars"].append({
    "title":"VW",
    "price":900
})

# Запишем данные в файл
# with open("cars.json","w") as file:
#     json.dump(shop,file,indent=4)


# Чтение данных из Json файла

with open("cars.json", "r") as file:
    #Получили словарь на основе файла с json данными
    cars_dict = json.load(file)
    pprint(cars_dict)