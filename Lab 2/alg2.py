def tribonacci(n):
    # Базовые случаи
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Рекурсивный случай
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Пример использования
n = 5  # Например, для n = 5
print(tribonacci(n))  # Выводит 4