class University:

    def __init__(self, title):
        self.title = title
        self.faculties = {}

    def __str__(self):
        return self.title

    def get_statistic(self):
        """Получение статистики работы университета"""
        students_count = 0
        result = f"\n{str(self):*^40}\n"
        for faculty in self.faculties.values():
            students_count += len(faculty.students)
        result += f"Факультетов: {len(self.faculties.keys())}\nСтудентов: {students_count}"
        for faculty in self.faculties.values():
            result += faculty.get_statistic()
        return result

    def add_faculty(self, faculty):
        """Добавление факультета"""
        self.faculties[faculty.title] = faculty


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


class Student:
    count = 0

    def __init__(self, name, surname, course, faculty):
        Student.count += 1
        self.name = name
        self.surname = surname
        self.course = course
        self.faculty = faculty
        self.grades = {}
        for subject in self.faculty.subjects:
            self.grades[subject] = []

    def __str__(self):
        return f"{self.surname} {self.name} ({self.course} курс)"

    def get_statistic(self):
        """Статистика успеваемости студента"""
        result = f'\n{str(self)}:\n'
        for subject, grades in self.grades.items():
            result += f"\t{subject:.<15}{self.get_average_grade(subject)}\tОценки: {tuple(grades)}\n"
        return result

    def add_grade(self, subject, grade):
        """Добавление оценки студенту по предмету"""
        self.grades[subject].append(grade)

    def get_average_grade(self, subject):
        """Расчет среднего балла """
        average_grade = sum(self.grades[subject]) / len(self.grades[subject])
        return format(average_grade, '.1f')


if __name__ == "__main__":
    mgu = University("MGU")
    urFak = Faculty('ЮрФак', mgu)
    mgu.add_faculty(urFak)
    urFak.add_subject('Юриспруденция')
    student = Student("Иван", "Иванов", 3, urFak)
    student.add_grade('Юриспруденция', 4)
    student.add_grade('Юриспруденция', 5)
    student.add_grade('Юриспруденция', 4)
    print(student)
    print(student.get_statistic())
    print(student.faculty)
    print(student.faculty.get_statistic())
    print(student.faculty.university)
    print(student.faculty.university.get_statistic())
    print(Student.count, Faculty.count)
