class Person:
    def __init__(self,fio,age):
        self.age = age
        self.fio = fio
    @staticmethod
    def show_difference_age(man1,man2):
        if man1.age == man2.age:
            print('Ровесники')
        else:
            if man1.age > man2.age:
                print(f"{man1.fio} старше {man2.fio} на {man1.age - man2.age}")
            else:
                print(f"{man2.fio} старше {man1.fio} на {man2.age - man1.age}")

    # def show_difference_age(self,man2):
    #     if self.age == man2.age:
    #         print('Ровесники')
    #     else:
    #         if self.age > man2.age:
    #             print(f"{self.fio} старше {man2.fio} на {self.age - man2.age}")
    #         else:
    #             print(f"{man2.fio} старше {self.fio} на {man2.age - self.age}")

man1 = Person("Иван",30)
man2 = Person("Игорь",40)
# man1.show_difference_age(man2)

Person.show_difference_age(man1,man2)
