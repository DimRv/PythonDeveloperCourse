from abc import ABC, abstractmethod


class RealObject(ABC):
    @abstractmethod
    def do_something(self):
        pass

class RealObjectImpl(RealObject):
    def do_something(self):
        print('Выполняется взаимодействие с реальным объектом')

class RealObjectProxy(RealObjectImpl):
    def do_something(self):
        print("Выполняем предварительные действия")
        #Можно добавить условия при которых инстуркция ниже работает не каждый раз
        super().do_something()

client = RealObjectProxy()
client.do_something()