class Person:
    # self - это ссылка на объект, который запускает конструктор
    def __init__(self,id,fio,salary):
        self.salary = salary
        self.fio = fio
        self.id = id

    def add_bonus(self,size_bonus):
        self.salary += size_bonus

    def __str__(self):
        return f"Сотрудник {self.fio} зарабатывает {self.salary}"



person1 = Person(1,"Иванов",100_000)
person1.add_bonus(50000)
person2 = Person(2,"Петров",170_000)
person3 = Person(3,"Сидоров",160_000)

men = [person1,person2,person3]
for man in men:
    print(man)