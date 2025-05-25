from abc import ABC, abstractmethod


class CarBuilder(ABC):

    @abstractmethod
    def add_engine(self, value):
        pass

    @abstractmethod
    def add_body(self, value):
        pass


class Car(CarBuilder):

    def __init__(self, title):
        self.title = title
        self.isEngine = False

    def add_engine(self, value):
        self.isEngine = False,
        self.__setattr__('engine', value)
        return self

    def add_body(self, value):
        self.__setattr__('body', value)
        return self

    def start_engine(self):
        if self.isEngine:
            if not self.isEngine[0]:
                self.isEngine = True,
                print('Двигатель запущен')
            else:
                print("Двигатель уже был запущен")
        else:
            print("Запуск двигателя не возможен из за его отсутствия")

    def stop_engine(self):
        if self.isEngine:
            if self.isEngine[0]:
                self.isEngine = False,
                print('Двигатель заглушен')
            else:
                print("Двигатель уже был заглушен")
        else:
            print("Остановка двигателя не возможна из за его отсутствия")

    def __str__(self):
        return self.title

    def get_info(self):
        result = f'{self}\n'
        if hasattr(self, 'body'):
            result += f"{self.body}\n"
        if hasattr(self, 'engine'):
            result += f'Имеет {self.engine} в '
            result += "запущенном " if self.isEngine[0] else "выключенном "
            result += 'состоянии\n'
        else:
            result += 'в разобранном состоянии'
        return result





