# Zd.5.2

subjects = ["география", "труд", "информатика", "химия", "ботаника", "литература"]

print("Школьные предметы:", ", ".join(subjects))
disliked_subjects = input("Введите названия предметов, которые вам не нравятся (через запятую): ").split(',')
disliked_subjects = [subject.strip().lower() for subject in disliked_subjects]
subjects = [sub for sub in subjects if sub.lower() not in disliked_subjects]
#
# print("Остались любимые предметы:", subjects)