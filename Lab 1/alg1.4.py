import time
import matplotlib.pyplot as plt

# Определение функции foo
def foo(n):  # n - число
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1
        if divisors == 0:
            res.append(i)
    return res

# Функция для измерения времени выполнения функции foo
def measure_time(n):
    start_time = time.perf_counter()
    foo(n)
    end_time = time.perf_counter()
    return end_time - start_time

# Генерация данных для графика
input_sizes = range(1, 1001, 50)  # Значения n от 1 до 1000 с шагом 50
execution_times = [measure_time(size) for size in input_sizes]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='r', label='Время выполнения foo(n)')
plt.title('Зависимость времени выполнения функции foo от значения n')
plt.xlabel('Значение n')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()
plt.show()
