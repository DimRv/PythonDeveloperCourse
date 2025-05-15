class Student:
    def __init__(self,fio,course,faculty):
        self.faculty = faculty
        self.course = course
        self.fio = fio

    def __str__(self):
        return f"Студент учится на {self.course} курсе, на факульте {self.faculty.title}"