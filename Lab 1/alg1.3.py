import time
import matplotlib.pyplot as plt

# Определение функции foo
def foo(s):  # s - строка
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

# Функция для измерения времени выполнения функции foo
def measure_time(length):
    s = 'a' * (length // 2) + '1' * (length // 2)  # Строка из 'a' и '1' длиной length
    start_time = time.perf_counter()
    foo(s)
    end_time = time.perf_counter()
    return end_time - start_time

# Генерация данных для графика
input_sizes = range(1, 10001, 500)  # Длины строк от 1 до 10,000 с шагом 500
execution_times = [measure_time(size) for size in input_sizes]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b', label='Время выполнения foo(s)')
plt.title('Зависимость времени выполнения функции foo от длины строки')
plt.xlabel('Длина строки (количество символов)')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()
plt.show()
