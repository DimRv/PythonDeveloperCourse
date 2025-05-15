"""
Здесь все объекты в отдельном модуле

Вопрос остается:
нормальная ли практика, что не возможно создать объект Студента без Университета и Факультета?

Если да, то как правильно ограничивать доступ Студента к определенным методам?
через __getattr__()?
"""


from random import choice, randint
import Univer


names = ["Иван", "Дмитрий", "Николай", "Олег", "Александр", "Алексей", "Петр"]
surnames = ["Иванов", "Петров", "Сидоров", "Романов", "Смирнов", "Семенов"]

# Создаем Университет
spb_gu = Univer.University("СБПГУ")
# Добавляем два Факультета
for faculty in ("ФизМат", "ЮрФак"):
    spb_gu.add_faculty(Univer.Faculty(faculty, spb_gu))
# Добавляем предметы к каждому факультету
for subject in ("МатАн", "Информатика"):
    spb_gu.faculties['ФизМат'].add_subject(subject)
for subject in ("Право", "История"):
    spb_gu.faculties['ЮрФак'].add_subject(subject)

# Добавляем каждому факультету студентов, а каждому студенту баллы успеваемости
for _ in range(randint(10, 15)):
    faculty = spb_gu.faculties[choice(list(spb_gu.faculties))]
    student = Univer.Student(choice(names), choice(surnames), randint(1, 5), faculty)
    faculty.add_student(student)
    for subject in faculty.subjects:
        for _ in range(randint(2, 4)):
            student.add_grade(subject, randint(2, 5))

# Выводим статистику Университета
print(spb_gu.get_statistic())

# Получаем общее кол-во созданных объектов Студентов
print(Univer.Student.count)

# Студент имеет связь с факультетом, а факультет с Университетом
student = spb_gu.faculties['ЮрФак'].students[1]
print(student, student.faculty, student.faculty.university)
# Через студента можно получить информацию о статистике успеваемости всего факультета.
print("!"*40)
print(student.faculty.get_statistic())
