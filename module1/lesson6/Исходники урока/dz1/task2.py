"""
Создайте список с названиями шести школьных предметов. Спросите у пользователя,
какие из этих предметов ему не нравятся. Удалите выбранные предметы из списка и
выведите его повторно

Решение с дополнительными вставками
"""

lessons = ["математика", 'физика', 'литература', 'химия', 'музыка', 'субботник']
disliked_lessons = input(f"Какие из этих уроков Вам не нравятся? (Перечислите через пробел):\n"
                         f"{" ".join(lessons)}\n").lower().strip()
for disliked_lesson in disliked_lessons.split():
    if disliked_lesson not in lessons:
        print(f"Вам повезло! Урок {disliked_lesson} и так не входит в программу! :)")
    elif disliked_lesson == 'субботник':
        print(f"Нет уж! Субботник ОБЯЗАТЕЛЕН!")
    else:
        lessons.remove(disliked_lesson)
print(f"Ваша программа:\n{' '.join(lessons)}")
