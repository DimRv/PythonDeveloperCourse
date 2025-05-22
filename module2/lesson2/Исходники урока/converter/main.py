# Инициализация значений курсов
from converter.Converter import Converter
from converter.Valute import Valute

valute1 = Valute("baks",85)
valute2 = Valute("euro",95)
valute3 = Valute("rub",1)

# 100 долларов в евро
print(Converter.convert(valute1,valute2,100))

#100 долларов в рубли
print(Converter.convert(valute1,valute3,100))

# 1 евро в доллары
print(Converter.convert(valute2,valute1,1))