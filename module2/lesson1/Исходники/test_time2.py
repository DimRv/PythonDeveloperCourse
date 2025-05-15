import time

# start_time = time.time()
#
# my_list = []
# for i in range(100_000):
#     my_list.append(i)
#
# end_time = time.time()
# exec_time = end_time - start_time
# print(f"Время выполнения: {exec_time:.4f} секунд")

# Более точный способ вывода времени

start_time = time.perf_counter()

my_list = []
for i in range(100_000):
    my_list.append(i)

end_time = time.perf_counter()
exec_time = end_time - start_time
print(f"Время выполнения: {exec_time:.6f} секунд")