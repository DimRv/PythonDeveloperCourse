class Univer:
    def __init__(self,title_univer,faculties,students):
        self.students = students
        self.faculties = faculties
        self.title_univer = title_univer

    def show_info(self):
        print(f"В универе {self.title_univer} есть {", ".join(self.faculties)}")
