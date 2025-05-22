class Person:
    # Если необходимо доступ к свойству закрывать - используте __ перед название свойства
    def __init__(self,fio,salary):
        self.__salary = salary
        self.__fio = fio

    def set_fio(self,fio):
        self.__fio = fio

    def set_salary(self,salary):
        password = input('Введите пароль для возможности изменить оклад')
        if password == "111":
            self.__salary = salary
            return
        print("Доступ запрещен!")


    def get_fio(self):
        return self.__fio

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f"Сотрудник {self.__fio} зарабатывает {self.__salary}"

man = Person("Иванов",100_000)
# man.__salary += 200_000
man.set_salary(500_000)

print(man)

# print(man.get_fio() + " сотрудник компании")