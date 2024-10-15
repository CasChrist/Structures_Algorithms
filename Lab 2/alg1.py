import random
import time
import matplotlib.pyplot as plt

# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Функция для замера времени
def time_sort(sort_func, data):
    start_time = time.time()
    sort_func(data)
    return time.time() - start_time

# Проведение экспериментов
sizes = [100, 200, 300, 400, 500]
selection_times = []
quick_times = []

for size in sizes:
    # Случайный список
    random_list = [random.randint(0, 1000) for _ in range(size)]
    selection_times.append(time_sort(selection_sort, random_list.copy()))
    quick_times.append(time_sort(quick_sort, random_list.copy()))

# Построение графиков
plt.figure(figsize=(12, 6))

# Случайные числа
plt.subplot(1, 3, 1)
plt.plot(sizes, selection_times, label='Сортировка выбором')
plt.plot(sizes, quick_times, label='Быстрая сортировка')
plt.title('Случайные числа')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()

# Отсортированный список
sorted_list = [i for i in range(500)]
selection_times_sorted = [time_sort(selection_sort, sorted_list) for _ in sizes]
quick_times_sorted = [time_sort(quick_sort, sorted_list) for _ in sizes]

plt.subplot(1, 3, 2)
plt.plot(sizes, selection_times_sorted, label='Сортировка выбором')
plt.plot(sizes, quick_times_sorted, label='Быстрая сортировка')
plt.title('Отсортированный список')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()

# Обратно отсортированный список
reverse_sorted_list = sorted_list[::-1]
selection_times_reverse_sorted = [time_sort(selection_sort, reverse_sorted_list) for _ in sizes]
quick_times_reverse_sorted = [time_sort(quick_sort, reverse_sorted_list) for _ in sizes]

plt.subplot(1, 3, 3)
plt.plot(sizes, selection_times_reverse_sorted, label='Сортировка выбором')
plt.plot(sizes, quick_times_reverse_sorted, label='Быстрая сортировка')
plt.title('Обратно отсортированный список')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()

plt.tight_layout()
plt.show()