class Person:
    count = 0
    def __init__(self,fio,position):
        self.position = position
        self.fio = fio
        Person.count += 1
        self.id = Person.count
        self.salary = position.salary_post


    def __str__(self):
        return (f"Сотрудник (id={self.id})  {self.fio} зарабатывает {self.salary}"
                f" в должности {self.position.title_post}")




