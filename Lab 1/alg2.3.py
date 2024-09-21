import random, time
import matplotlib.pyplot as plt

# Алгоритм 1: Через сортировку
def find_top_three_sort(arr):
    if len(arr) < 3:
        return sorted(arr, reverse=True)
    return sorted(arr, reverse=True)[:3]

# Алгоритм 2: Линейный поиск трех максимальных значений
def find_top_three_linear(arr):
    if len(arr) < 3:
        return sorted(arr, reverse=True)
    
    first = second = third = float('-inf')
    
    for num in arr:
        if num > first:
            first, second, third = num, first, second
        elif num > second:
            second, third = num, second
        elif num > third:
            third = num
    
    return [first, second, third]

# Функция для измерения времени выполнения
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# Подготовка данных для тестирования
sizes = [100, 1000, 5000, 10000, 50000, 100000, 200000]
times_sort = []
times_linear = []

# Генерация случайных данных и замер времени
for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    
    # Время для алгоритма 1 (сортировка)
    time_sort = measure_time(find_top_three_sort, arr)
    times_sort.append(time_sort)
    
    # Время для алгоритма 2 (линейный поиск)
    time_linear = measure_time(find_top_three_linear, arr)
    times_linear.append(time_linear)

# Построение графика
plt.plot(sizes, times_sort, label="Через сортировку (O(n log n))")
plt.plot(sizes, times_linear, label="Линейный поиск (O(n))")
plt.xlabel("Количество элементов")
plt.ylabel("Время (в секундах)")
plt.title("Сравнение времени выполнения двух алгоритмов")
plt.legend()
plt.grid(True)
plt.show()
