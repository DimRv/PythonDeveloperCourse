class Test:
    def __init__(self):
        self.x = 0
    def f(self):
        self.x += 1
        print(self.x)

    @staticmethod
    def test():
        """Из static метода вызываем методы объекта через объект"""
        Test().f()

obj1  = Test()
obj2  = Test()

obj1.f()
obj1.f()

obj2.f()
obj2.f()