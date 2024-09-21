import time
import matplotlib.pyplot as plt

# Алгоритм 1: Сравнение строки с её обратной версией
def is_palindrome_reverse(s):
    s = s.lower()  # Игнорируем регистр
    s = ''.join(c for c in s if c.isalnum())  # Игнорируем пробелы и знаки препинания
    return s == s[::-1]

# Алгоритм 2: Два указателя
def is_palindrome_two_pointers(s):
    s = s.lower()  # Игнорируем регистр
    s = ''.join(c for c in s if c.isalnum())  # Игнорируем пробелы и знаки препинания
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Функция для измерения времени выполнения
def measure_time(func, s):
    start_time = time.time()
    func(s)
    end_time = time.time()
    return end_time - start_time

# Генерация строк разной длины для тестирования
sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
times_reverse = []
times_two_pointers = []

# Генерация строк и замер времени
for size in sizes:
    test_str = "a" * (size - 1) + "b"  # Создаем строку заданной длины, почти палиндром
    time_reverse = measure_time(is_palindrome_reverse, test_str)
    times_reverse.append(time_reverse)
    
    time_two_pointers = measure_time(is_palindrome_two_pointers, test_str)
    times_two_pointers.append(time_two_pointers)

# Построение графика
plt.plot(sizes, times_reverse, label="Сравнение с обратной версией (O(n))")
plt.plot(sizes, times_two_pointers, label="Два указателя (O(n))")
plt.xlabel("Длина строки")
plt.ylabel("Время (в секундах)")
plt.title("Сравнение времени выполнения алгоритмов палиндрома")
plt.legend()
plt.grid(True)
plt.show()
