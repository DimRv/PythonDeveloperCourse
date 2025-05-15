class Faculty:
    count = 0

    def __init__(self, title, university):
        self.title = title
        self.university = university
        self.subjects = []
        self.students = []
        Faculty.count += 1

    def __str__(self):
        return self.title

    def get_statistic(self):
        """Статистика работы факультета"""
        result = f'\n{str(self):-^40}\n'
        result += f"Предметов: {len(self.subjects)}\n"
        result += f"Студентов: {len(self.students)}\n"
        for student in self.students:
            result += student.get_statistic()
        return result

    def add_subject(self, subject):
        """Добавление предмета"""
        self.subjects.append(subject)

    def add_student(self, student):
        """Добавление студента"""
        self.students.append(student)

