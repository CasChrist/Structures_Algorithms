import time
import matplotlib.pyplot as plt
import numpy as np

# Алгоритм 1: N^2 - N - 10
def T1(N):
    return N**2 - N - 10

# Алгоритм 2: 4N + 40
def T2(N):
    return 4 * N + 40

# Проверка времени выполнения для каждого алгоритма
def measure_time(func, N):
    start_time = time.time()
    result = func(N)
    end_time = time.time()
    return end_time - start_time

# Проверяем, что при N = 10 время выполнения одинаково
N_equal = 10
t1_value = T1(N_equal)
t2_value = T2(N_equal)

print(f"При N = {N_equal}: T1(N) = {t1_value}, T2(N) = {t2_value}")

# Теперь строим график для разных размеров массива
sizes = np.arange(1, 50, 1)  # Массив размеров от 1 до 50
times_t1 = [T1(N) for N in sizes]
times_t2 = [T2(N) for N in sizes]

# Построение графика
plt.plot(sizes, times_t1, label="T1(N) = N^2 - N - 10")
plt.plot(sizes, times_t2, label="T2(N) = 4N + 40")
plt.axvline(x=N_equal, color='r', linestyle='--', label=f'N = {N_equal}')
plt.xlabel("Размер массива (N)")
plt.ylabel("Количество операций")
plt.title("Сравнение количества операций двух алгоритмов")
plt.legend()
plt.grid(True)
plt.show()
