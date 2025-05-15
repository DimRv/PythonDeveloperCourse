import timeit

my_code = """
x = list(range(100))
y = []
for i in x:
   y.append(i * 2)
"""

print(timeit.timeit(my_code,number=100) / 100)