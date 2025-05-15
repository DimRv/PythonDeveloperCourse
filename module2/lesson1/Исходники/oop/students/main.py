from oop.students.Faculty import Faculty
from oop.students.Student import Student
from oop.students.Univer import Univer

univer = Univer("МГУ",[Faculty(1,"Мех-мат"),
                       Faculty(2,"Физ-мат")],[Student("Иванов",5,
                                                    Faculty(2,"Физ-мат"))])

univer.show_info()