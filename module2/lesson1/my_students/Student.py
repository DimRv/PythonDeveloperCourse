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

