str = "abcdef"
# print(str[3]) #d

# print(str[:2]) #ab
# print(str[3:]) #def
# print(str[::2]) #ace

# str[0] = 's' #будет ошибка, т.к. строка имутабельна, т.е. неизменная
# Менять символы в строке нельзя, можно лишь считывать

# print(str[len(str) - 1])

# print("Проект \"САОС\" - самый успешный проект компании")
# print('Проект "САОС" - самый успешный проект компании')

# Все команды, они же действия, которые встроены в язык делятся на 2 вида:
# 1) Функции
# 2) Методы

# Функция - это универсальная команда, она не связана ни с каким объектом
# Метод - это функция объекта, она запускается через оператор точка после имени объекта,
# к которому она привязана

# Базовые методы для работы со строками

# test = "добрый вечер"
# Регистровые методы
# print(test.title()) #каждое слово будет начинаться с верхнего регистра
# print(test.capitalize()) #Первое слово в строке преобразуется к верхнему регистру

# Поиск в строке
# 1) Метод find ищет подстроку в строке и если найдет, то вернет в качестве
# результата индекс первого вхождения подстроки в строке. А если не нашел, то вернет -1
s = "Hello world"
# print(s.find('o'))



# print("Найдено" if s.find("x") != -1 else "Не найдено")

# 2) Оператор in

# print("o" in s)

# 3) Метод count - возвращает количество найденных подстрок

# phones = "+79234234230, +79234234231, +79234234232"
# print("В строке содержится", phones.count("+"),"телефонов")

# Удаление подстроки из строки
# Метод strip без параметров - удаляет пробелы в начале и в конце строки

# print("  test   ".strip()) #удалили пробелы в начале и в конце строки
# print("+79234234230, +79234234231, +79234234232".strip("+"))
# Если в strip находится параметр равный первому и последнему символу встроке,
# то он их удаляет оба
# print("besab".strip("b")) #esa
# print("    test".lstrip()) #удаляем все пробелы слева
# print("test    ".rstrip()) #удаляем все пробелы справа

fio = "Иванов Иван Иванович"
# Для преобразования строки в список строк используйте метод split. В данном методе
# в качестве параметра передаем символ или подстроку, которая является разделителем
# в строке

# mas_fio = fio.split(" ")
# print(mas_fio)
# print("Привет,",fio.split()[1])

# Преобразование списка строк в одну строку

test_list = ["Привет!","Как","дела?"]
print(" ".join(test_list))