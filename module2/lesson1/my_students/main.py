"""
Добрый день!

Хочется чтобы модули содержали в себе объекты не зависящие от других модулей.
Суть модуля же - возможность его загрузки в любом коде

На лекции мы выделали классы в отдельные модули, здесь реализовал такой же подход, но получается
зависимость одного модуля от другого.

И противоположный вопрос:
Может ли вообще существовать объект Студент не зависимо от объектов Университет и Факультет?

В коде ниже для создания экземпляра объекта Студент нужно обязательно иметь Объект-Университет
и Объект-Факультет.

И Студент не может быть загружен не зависимо от Универа и Факультета
"""


from random import choice, randint
from Faculty import Faculty
from Student import Student
from University import University


names = ["Иван", "Дмитрий", "Николай", "Олег", "Александр", "Алексей", "Петр"]
surnames = ["Иванов", "Петров", "Сидоров", "Романов", "Смирнов", "Семенов"]

# Создаем Университет
spb_gu = University("СБПГУ")
# Добавляем два Факультета
for faculty in ("ФизМат", "ЮрФак"):
    spb_gu.add_faculty(Faculty(faculty, spb_gu))
# Добавляем предметы к каждому факультету
for subject in ("МатАн", "Информатика"):
    spb_gu.faculties['ФизМат'].add_subject(subject)
for subject in ("Право", "История"):
    spb_gu.faculties['ЮрФак'].add_subject(subject)

# Добавляем каждому факультету студентов, а каждому студенту баллы успеваемости
for _ in range(randint(10, 15)):
    faculty = spb_gu.faculties[choice(list(spb_gu.faculties))]
    student = Student(choice(names), choice(surnames), randint(1, 5), faculty)
    faculty.add_student(student)
    for subject in faculty.subjects:
        for _ in range(randint(2, 4)):
            student.add_grade(subject, randint(2, 5))

# Выводим статистику Университета
print(spb_gu.get_statistic())
