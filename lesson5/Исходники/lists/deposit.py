names = ["Иван","Олег","Роман"]
money = [100_000,300_000,200_000]
years = [5,3,2]

def show_profit(money,years):
    rate = 25 if years > 3 else 20
    for year in range(1,years + 1):
        profit = int(money * rate / 100) #ежегодная прибыль
        money += profit
        print(f"За {year} год Ваша прибыль составила: {profit}, сумма: {money}")

for i in range(0,len(names)):
    print(f"Клиент {names[i]} (сумма: {money[i]}, срок вклада: {years[i]})")
    show_profit(money[i],years[i])
    print("*" * 50)

