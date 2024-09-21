import random, time
import matplotlib.pyplot as plt

# Алгоритм 1: Один проход по списку
def find_min_max_single_pass(arr):
    if not arr:
        return None, None
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

# Алгоритм 2: Два отдельных поиска
def find_min_max_two_searches(arr):
    if not arr:
        return None, None
    min_val = min(arr)
    max_val = max(arr)
    return min_val, max_val

# Функция для измерения времени выполнения
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# Подготовка данных для тестирования
sizes = [100, 1000, 5000, 10000, 50000, 100000, 200000]
times_single_pass = []
times_two_searches = []

# Генерация случайных данных и замер времени
for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    
    # Время для алгоритма 1
    time_single = measure_time(find_min_max_single_pass, arr)
    times_single_pass.append(time_single)
    
    # Время для алгоритма 2
    time_two = measure_time(find_min_max_two_searches, arr)
    times_two_searches.append(time_two)

# Построение графика
plt.plot(sizes, times_single_pass, label="Один проход по списку (O(n))")
plt.plot(sizes, times_two_searches, label="Два отдельных поиска (O(n))")
plt.xlabel("Количество элементов")
plt.ylabel("Время (в секундах)")
plt.title("Сравнение времени выполнения двух алгоритмов")
plt.legend()
plt.grid(True)
plt.show()
