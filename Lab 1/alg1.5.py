import time
import matplotlib.pyplot as plt

# Определение функции foo
def foo(nums):  # nums - список
    for x in nums:
        if x % 2 == 0:
            return True
    else:
        return False

# Функция для измерения времени выполнения функции foo
def measure_time(length):
    nums = [1] * length  # Создаем список длиной `length`, состоящий из нечетных чисел
    start_time = time.perf_counter()
    foo(nums)
    end_time = time.perf_counter()
    return end_time - start_time

# Генерация данных для графика
input_sizes = range(1, 7000001, 500000)  # Длины списка от 1 до 10,000 с шагом 500
execution_times = [measure_time(size) for size in input_sizes]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='g', label='Время выполнения foo(nums)')
plt.title('Зависимость времени выполнения функции foo от длины списка')
plt.xlabel('Длина списка (количество элементов)')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()
plt.show()
