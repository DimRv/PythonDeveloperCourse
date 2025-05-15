from Position import Position
from Person import Person

position1 = Position(1,"Программист",200_000)
position2 = Position(2,"DevOps",220_000)

man1 = Person("Иванов",position1)
man2 = Person("Петров",position2)
man3 = Person("Сидоров",position1)

men = [man1,man2,man3]
for man in men:
    print(man)