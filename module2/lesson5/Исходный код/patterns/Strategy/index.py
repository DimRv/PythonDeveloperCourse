 # Стратегия определяет семейство алгоритмов, которые являются взаимозаменяемыми.
# Стратегия позволяет менять поведение на основе параметра метода
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse(self,path):
        pass

class ParserForXml(Parser):
    def parse(self,path):
        print("Здесь выполняется алгоритм извлечения данных из документа XML")

class ParserForJSON(Parser):
    def parse(self,path):
        print("Здесь выполняется алгоритм извлечения данных из документа JSON")

class StrategyImp():
    @staticmethod
    def parse_doc(file_name):
        ext = file_name.split('.')[-1]
        match ext:
            case 'xml':
                return ParserForXml().parse(file_name)
            case 'json':
                return ParserForJSON().parse(file_name)
            case _:
                print("Документ не распознан")

StrategyImp.parse_doc("test.xml")