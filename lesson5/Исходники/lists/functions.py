from random import randint

def show_persons(salaries:list)->None:
    for number,salary in enumerate(salaries,1):
        print(f"Сотрудник №{number} имеет оклад: {salary}")
    print("*" * 50)
    print(f"Максимальный оклад в офисе: {get_max_salary(salaries)}")
    print("*" * 50)

def get_max_salary(salaries:list)->int:
    max_salary = salaries[0]
    for i in range(1,len(salaries) - 1):
        if max_salary < salaries[i]:
            max_salary = salaries[i]
    return max_salary





def get_office(address:str,count_men:int)->list:
    print(f"По адресу {address} работают {count_men} сотрудников")
    """Заполняем список зарплатами сотрудников"""
    salaries = [randint(100000,300000) for _ in range(count_men)]
    return salaries

office1 = get_office("Московская 8",15)
office2 = get_office("Чапаева 1",5)

show_persons(office1)

show_persons(office2)

# print(max(max(office1),max(office2)))