# Оператор match/case, когда нужно проверить совпадение значения, находящегося
# после match с разными вариантами, которые указываем после case

# color = input("Какой цвет сейчас горит у светофора? (red,green,yellow)")
#

mas = ['red','green','yellow']
color = input("Какой цвет сейчас горит у светофора? (red,green,yellow)")
print("Ввели корректный цвет" if color in mas else "Некорректный цвет")
#
# match color:
#     case "green":
#         print("Вперед")
#     case "red":
#         print("Стоп")
#     case "yellow":
#         print("Внимание")
#     case _:
#         print("Поломка светофора")

# match input("Какой сегодня день?"):
#     case "1" | "Понедельник" | "Monday":
#         print("Верно, сегодня понедельник")
#     case _:
#         print("Вы ошиблись!")
#
