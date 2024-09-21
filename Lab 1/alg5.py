import time
import matplotlib.pyplot as plt

# Функция для замера времени операции 'in' в списке
def measure_in_list(n):
    lst = list(range(n))
    start_time = time.time()
    _ = n - 1 in lst  # Проверка наличия элемента в списке
    end_time = time.time()
    return end_time - start_time

# Функция для замера времени операции 'in' в множестве
def measure_in_set(n):
    st = set(range(n))
    start_time = time.time()
    _ = n - 1 in st  # Проверка наличия элемента в множестве
    end_time = time.time()
    return end_time - start_time

# Диапазон значений N (размер данных)
sizes = [100, 500, 1000, 5000, 10000, 50000, 100000, 200000, 500000]

# Списки для хранения времени выполнения операции 'in'
times_list = []
times_set = []

# Замер времени для каждой N
for n in sizes:
    time_list = measure_in_list(n)
    times_list.append(time_list)
    
    time_set = measure_in_set(n)
    times_set.append(time_set)

# Построение графика
plt.plot(sizes, times_list, label="Операция 'in' в списке")
plt.plot(sizes, times_set, label="Операция 'in' в множестве")
plt.xlabel("Размер данных (N)")
plt.ylabel("Время операции 'in' (в секундах)")
plt.title("Сравнение времени выполнения операции 'in' для списков и множеств")
plt.legend()
plt.grid(True)
plt.show()
