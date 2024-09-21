import random, time
import matplotlib.pyplot as plt

# Алгоритм 1: Через множество
def all_unique_set(arr):
    return len(arr) == len(set(arr))

# Алгоритм 2: Вложенные циклы
def all_unique_loops(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True

# Функция для измерения времени выполнения
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# Подготовка данных для тестирования
sizes = [100, 1000, 5000, 10000, 20000, 30000, 40000]
times_set = []
times_loops = []

# Генерация случайных данных и замер времени
for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    
    # Время для алгоритма 1 (через множество)
    time_set = measure_time(all_unique_set, arr)
    times_set.append(time_set)
    
    # Время для алгоритма 2 (вложенные циклы)
    time_loops = measure_time(all_unique_loops, arr)
    times_loops.append(time_loops)

# Построение графика
plt.plot(sizes, times_set, label="Проверка через множество (O(n))")
plt.plot(sizes, times_loops, label="Проверка через вложенные циклы (O(n^2))")
plt.xlabel("Количество элементов")
plt.ylabel("Время (в секундах)")
plt.title("Сравнение времени выполнения двух алгоритмов")
plt.legend()
plt.grid(True)
plt.show()
