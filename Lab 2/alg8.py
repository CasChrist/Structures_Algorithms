def print_sudoku(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def is_valid(matrix, row, col, num):
    # Проверка строки
    if num in matrix[row]:
        return False

    # Проверка столбца
    for r in range(4):
        if matrix[r][col] == num:
            return False

    # Проверка 2x2 квадрата
    start_row = row - row % 2
    start_col = col - col % 2
    for r in range(2):
        for c in range(2):
            if matrix[r + start_row][c + start_col] == num:
                return False

    return True

def find_empty(matrix):
    for r in range(4):
        for c in range(4):
            if matrix[r][c] == 0:  # 0 означает пустую клетку
                return r, c  # Возвращает координаты пустой клетки
    return None  # Нет пустых клеток

def solve_sudoku(matrix):
    empty = find_empty(matrix)
    if not empty:
        return True  # Базовый случай: нет пустых клеток, судоку решено

    row, col = empty  # Получаем координаты пустой клетки

    for num in range(1, 5):  # Пробуем числа от 1 до 4
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num  # Пробуем число
            if solve_sudoku(matrix):  # Рекурсивно пытаемся решить дальше
                return True
            matrix[row][col] = 0  # Возврат: сбрасываем число, если не удалось

    return False  # Невозможно решить

# Исходное состояние мини-судоку
sudoku_matrix = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

if solve_sudoku(sudoku_matrix):
    print("Решенное мини-судоку:")
    print_sudoku(sudoku_matrix)
else:
    print("Нет решения.")
