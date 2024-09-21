import matplotlib.pyplot as plt
import time
import random

def foo(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

# Создадим данные для построения графика
sizes = [10, 50, 100, 200, 300, 500, 700, 1000, 2000, 5000]
times = []

# Замеряем время выполнения функции для различных размеров входного списка
for size in sizes:
    a = [random.randint(-100, 100) for _ in range(size)]
    start_time = time.time()
    foo(a)
    end_time = time.time()
    times.append(end_time - start_time)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linestyle='-', color='b', label='Bubble Sort (foo)')
plt.xlabel('Размер входного списка')
plt.ylabel('Время выполнения (секунды)')
plt.title('Зависимость времени выполнения функции foo от размера входных данных')
plt.grid(True)
plt.legend()
plt.show()
