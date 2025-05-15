def test_decorator(func):
    def action():
        print("Здесь будут выполняться действия до вызова основной функции")
        func()
        print("Действия после вызова функции")
    return action

@test_decorator
def f():
    print("Привет!")

f()