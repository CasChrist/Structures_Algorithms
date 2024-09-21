import random, string, time
from collections import Counter
import matplotlib.pyplot as plt

# Алгоритм 1: Использование Counter
def most_common_letter_counter(s):
    s = s.lower()  # Игнорируем регистр
    s = ''.join(c for c in s if c.isalpha())  # Оставляем только буквы
    counter = Counter(s)
    most_common = counter.most_common(1)[0]  # Получаем кортеж с наиболее частой буквой и её количеством
    return most_common

# Алгоритм 2: Использование стандартного словаря
def most_common_letter_dict(s):
    s = s.lower()  # Игнорируем регистр
    s = ''.join(c for c in s if c.isalpha())  # Оставляем только буквы
    freq = {}
    
    for letter in s:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    # Находим букву с максимальной частотой
    most_common_letter = max(freq, key=freq.get)
    return most_common_letter, freq[most_common_letter]

# Функция для измерения времени выполнения
def measure_time(func, s):
    start_time = time.time()
    func(s)
    end_time = time.time()
    return end_time - start_time

# Генерация случайных строк разной длины для тестирования
sizes = [1000, 5000, 10000, 50000, 100000, 200000, 500000]
times_counter = []
times_dict = []

# Генерация строк и замер времени
for size in sizes:
    test_str = ''.join(random.choices(string.ascii_letters + string.whitespace, k=size))  # Строка случайной длины
    
    # Время для алгоритма 1 (Counter)
    time_counter = measure_time(most_common_letter_counter, test_str)
    times_counter.append(time_counter)
    
    # Время для алгоритма 2 (словарь)
    time_dict = measure_time(most_common_letter_dict, test_str)
    times_dict.append(time_dict)

# Построение графика
plt.plot(sizes, times_counter, label="Использование Counter (O(n))")
plt.plot(sizes, times_dict, label="Использование словаря (O(n))")
plt.xlabel("Длина строки")
plt.ylabel("Время (в секундах)")
plt.title("Сравнение времени выполнения алгоритмов нахождения самой частой буквы")
plt.legend()
plt.grid(True)
plt.show()
