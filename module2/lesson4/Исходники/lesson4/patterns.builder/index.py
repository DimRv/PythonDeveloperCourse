from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build_bassein(self):
        pass

    @abstractmethod
    def build_garage(self):
        pass

    def build_roof(self):
        pass



class Bassein:
    def __init__(self,area):
        self.area = area

    def __str__(self):
        return f"Бассейн имеет площадь {self.area}"


class Garage:
    def __init__(self,type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return f"Гараж изготовлен из материала {self.type}, площадь гаража: {self.area}"

class Roof:
    def __init__(self,type):
        self.type = type

    def __str__(self):
        return f"Крыша изготовлена из материала {self.type}"

class Home(Builder):
    def build_bassein(self,type):
        self.__setattr__("bassein",Bassein(type))
        return self

    def build_garage(self,type, area):
        self.__setattr__("garage",Garage(type, area))
        return self

    def build_roof(self,type):
        self.__setattr__("roof",Roof(type))
        return self
    def show(self):
        if hasattr(self,"bassein"):
            print(f"Дом имеет бассейн. {self.bassein}")
        if hasattr(self,"garage"):
            print(f"Дом имеет гараж. {self.garage}")
        if hasattr(self,"roof"):
            print(f"Дом имеет крышу. {self.roof}")

home = Home().build_roof("Металлочерепица").build_garage("кирпич",30).build_bassein(100)
home.show()