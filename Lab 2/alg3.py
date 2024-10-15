def recursive_reverse(some_list):
    # Базовый случай
    if len(some_list) == 0:
        return []
    # Рекурсивный случай
    else:
        return [some_list[-1]] + recursive_reverse(some_list[:-1])

# Пример использования
result = recursive_reverse([1, 2, 3, 4, 5])
print(result)  # Выводит [5, 4, 3, 2, 1]
