abonents = {
    "Иванов":['+7923424223','+7923424221'],
    "Петров":['+7923424111','+7923424555','+7923424777'],
    "Сидоров":['+7923424000']
}

items = [
    {"id":1,
     "title":"",

     },
    {

    },
    {

    }
]



def show_abonents():
    info = ""

    for fio, phones in abonents.items():
        info += f"Абонент {fio} имеет "
        if len(phones) > 1:
            info += "номера телефонов:"
        else:
            info += "номер телефона:"
        info += ", ".join(phones) + "\n"  # преобразовали список в строку
    print(info)


def add_abonent():
    name = input("Введите имя абонента")
    list_phones = input("Введите список телефонов через запятую").split(",")
    abonents[name] = list_phones
    print("Абонент добавлен")


def remove_abonent():
    fio = input("Введите имя абонента для удаления")
    if fio in abonents:
        del abonents[fio]
        print("Абонент удален!")


while 1:
    answer = input("Выберите пункт меню:\n1) Вывести всех абонентов с телефонами\n"
                   "2) Добавить абонента и телефоны\n"
                   "3) Удалить абонента вместе с телефонами\n"
                   "4) Выход\n")

    match answer:
        case "1":
            show_abonents()
        case "2":
            add_abonent()
        case "3":
            remove_abonent()
        case "4":
            break