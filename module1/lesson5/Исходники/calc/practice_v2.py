# Пример консольного калькулятора

# def calc(sign):
#     match sign:
#         case "+":
#             return lambda a,b : a + b
#         case "-":
#             return lambda a,b : a - b
#         case "*":
#             return lambda a,b : a * b
#         case "/":
#             return lambda a,b : a / b if b != 0 else 777
#
# print(calc("*")(2,3))

# calc = lambda a,b,znak: a+b if znak=='+' else a-b if znak=='-' else a*b if znak=='*' else a/b if znak=='/' and b != 0 else None
# print(calc(7, 23, "+"))

# test = lambda sign, a, b : (a + b if sign == '+' else a - b if sign == '-' else a * b if sign == '*' else a / b if sign == '/' and b != 0 else None)

# print(test('*', 9, 0))

# lambda sign, a, b : (a + b if sign == '+' else a - b if sign == '-' else a * b if sign == '*' else a / b if sign == '/' and b != 0 else None)