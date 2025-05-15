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


