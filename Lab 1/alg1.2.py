import matplotlib.pyplot as plt
import time
import random

def foo(i): # i - число
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result

# Создадим данные для построения графика
sizes = [1000, 10000, 100000000, 1000000000000, 10000000000000000,
         100000000000000000000, 1000000000000000000000000]
times = []

# Замеряем время выполнения функции для различных размеров входного списка
for size in sizes:
    a = random.randint(size-100, size+100)
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
