clients = []
COUNT = 5
while 1:
    clients.append(input("Введите Ваше имя\n"))
    if len(clients) > COUNT:
        print(f"Может войти {clients.pop(0)}, готовится {clients[0]}")
