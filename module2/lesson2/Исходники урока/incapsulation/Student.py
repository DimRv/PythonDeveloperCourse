class Student:
    def __init__(self,fio,course):
        self.__course = course if Student.is_course(course) else 0
        self.__fio = fio
        self.__title = "МГУ"

    @staticmethod
    def is_course(course_number):
        return True if 1 <= course_number <= 5 else False

    @property
    def fio(self):
        return self.__fio

    @property
    def course(self):
        return self.__course

    # Без сеттера курс изменить нельзя!

    @course.setter
    def course(self,course):
        if Student.is_course(course):
            self.__course = course

    def show_info(self):
        if self.course == 0:
            print("Курс задан некорректно")
        else:
            print(f"{self.fio} учится в {self.__title} на {self.course} курсе")

#Настраиваем пример для запуска

student = Student("Иванов",4)
student.show_info()
student.course += 1
student.show_info()