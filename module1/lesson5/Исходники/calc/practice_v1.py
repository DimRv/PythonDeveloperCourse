# Пример консольного калькулятора

def sum(a,b):
    return a + b
def dif(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b if b != 0 else "На 0 делить нельзя"

def calc(sign,a,b):
    match sign:
        case "+":
            return sum(a,b)
        case "-":
            return dif(a, b)
        case "*":
            return mult(a, b)
        case "/":
            return div(a, b)

print(calc("+",2,4))