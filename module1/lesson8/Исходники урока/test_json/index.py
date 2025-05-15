import json
from pprint import pprint

cars = """{
    "cars":[
        {
            "id":1,
            "title":"Audi",
            "price":1000
        },
        {
            "id":2,
            "title":"BMW",
            "price":1200
        },
        {
            "id":3,
            "title":"VW",
            "price":900
        }
    ],
    "shop":{
        "shop_title":"Vip Car",
        "address":"Москва..."
    }
}
"""

# Конвертируем строку json в словарь

info = json.loads(cars)
pprint(info)

# print(info["cars"][1]["title"])

# for car in info['cars']:
#     print(f"Автомобиль {car['title']} стоит {car['price']}")

# Преобразование словаря в строку JSON

dict_to_json = json.dumps(info,indent=4,ensure_ascii=False)
print(dict_to_json)