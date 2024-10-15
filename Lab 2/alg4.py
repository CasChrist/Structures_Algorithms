import time
import matplotlib.pyplot as plt

# Функция для вычисления n-го числа Фибоначчи
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Функция для вычисления n-го числа Люка
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# Функция для вычисления n-го числа Фибоначчи с использованием чисел Люка
def fib_with_lucas(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = n // 2
        j = n - i
        Fi = fib_with_lucas(i)
        Lj = lucas(j)
        Fj = fib_with_lucas(j)
        Li = lucas(i)
        return (Fi + Lj) * (Fj + Li) // 2

# Функция для вычисления n-го числа Люка с использованием чисел Фибоначчи
def lucas_with_fib(n):
    if n == 0:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)

# Замеры времени для стандартных функций
n_values = list(range(30))
fib_times = []
lucas_times = []

for n in n_values:
    start_time = time.time()
    fibonacci(n)
    fib_times.append(time.time() - start_time)

    start_time = time.time()
    lucas(n)
    lucas_times.append(time.time() - start_time)

# Замеры времени для функций с использованием свойств
fib_lucas_times = []
lucas_fib_times = []

for n in n_values:
    start_time = time.time()
    fib_with_lucas(n)
    fib_lucas_times.append(time.time() - start_time)

    start_time = time.time()
    lucas_with_fib(n)
    lucas_fib_times.append(time.time() - start_time)

# Построение графиков
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(n_values, fib_times, label='Fibonacci (рекурсия)', marker='o')
plt.plot(n_values, lucas_times, label='Lucas (рекурсия)', marker='x')
plt.title('Время выполнения стандартных функций')
plt.xlabel('n')
plt.ylabel('Время (сек)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(n_values, fib_lucas_times, label='Fib with Lucas', marker='o')
plt.plot(n_values, lucas_fib_times, label='Lucas with Fib', marker='x')
plt.title('Время выполнения функций с использованием свойств')
plt.xlabel('n')
plt.ylabel('Время (сек)')
plt.legend()

plt.tight_layout()
plt.show()
