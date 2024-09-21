import time
import matplotlib.pyplot as plt

# Функция для замера времени удаления элемента из списка
def measure_del_list(n):
    lst = list(range(n))
    start_time = time.time()
    del lst[n // 2]  # Удаляем элемент из середины списка
    end_time = time.time()
    return end_time - start_time

# Функция для замера времени удаления элемента из словаря
def measure_del_dict(n):
    dct = {i: i for i in range(n)}
    start_time = time.time()
    del dct[n // 2]  # Удаляем элемент с ключом n // 2
    end_time = time.time()
    return end_time - start_time

# Диапазон значений N (размер данных)
sizes = [100, 500, 1000, 5000, 10000, 50000, 100000, 200000]

# Списки для хранения времени удаления
times_list = []
times_dict = []

# Замер времени для каждой N
for n in sizes:
    time_list = measure_del_list(n)
    times_list.append(time_list)
    
    time_dict = measure_del_dict(n)
    times_dict.append(time_dict)

# Построение графика
plt.plot(sizes, times_list, label="Удаление из списка (del)")
plt.plot(sizes, times_dict, label="Удаление из словаря (del)")
plt.xlabel("Размер данных (N)")
plt.ylabel("Время удаления (в секундах)")
plt.title("Сравнение времени удаления элемента из списка и словаря")
plt.legend()
plt.grid(True)
plt.show()
