class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """Добавляет новый элемент в начало списка"""
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def remove(self, item):
        """Удаляет элемент из списка"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:  # Удаление из начала списка
            self.head = current.next
        else:
            previous.next = current.next

    def search(self, item):
        """Ищет элемент в списке, возвращает True, если элемент найден"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def size(self):
        """Возвращает количество элементов в списке."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def pop(self, pos=None):
        """Удаляет и возвращает элемент на указанной позиции (по умолчанию последний)."""
        if self.is_empty():
            raise IndexError("Попытка удаления из пустого списка")

        if pos is None:
            pos = self.size() - 1  # По умолчанию удаляется последний элемент

        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        current = self.head
        previous = None
        index = 0
        while index < pos:
            previous = current
            current = current.next
            index += 1

        previous.next = current.next
        return current.data
    
    def append(self, item):
        """Добавляет элемент в конец списка."""
        temp = Node(item)
        
        # Если список пустой, добавляем элемент как голову
        if self.head is None:
            self.head = temp
        else:
            # Проходим до конца списка
            current = self.head
            while current.next is not None:
                current = current.next
            
            # Устанавливаем новый элемент как последний
            current.next = temp

    def __str__(self):
        """Возвращает строковое представление списка"""
        result = []
        current = self.head
        while current is not None:
            result.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(result) + "]"

class Stack:
    def __init__(self):
        """Инициализация стека"""
        self.items = UnorderedList()

    def isEmpty(self):
        """Проверка на пустоту стека"""
        return self.items.is_empty()

    def push(self, item):
        """Добавление элемента на вершину стека"""
        self.items.add(item)  # В стеке элемент добавляется на вершину, что в списке означает начало

    def pop(self):
        """Удаление элемента с вершины стека"""
        if not self.isEmpty():
            return self.items.pop(0)  # Удаление первого элемента (верхушки стека)
        else:
            raise IndexError("Попытка удаления из пустого стека")

    def peek(self):
        """Просмотр верхнего элемента стека"""
        if not self.isEmpty():
            return self.items.head.data  # Возврат первого элемента (верхушки)
        else:
            raise IndexError("Попытка просмотра верхнего элемента пустого стека")

    def size(self):
        """Возвращает количество элементов в стеке"""
        return self.items.size()

def evaluate_postfix(expression):
    """Оценивает выражение в обратной польской нотации."""
    stack = Stack()
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y if y != 0 else "Ошибка: деление на ноль"}

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # Если токен - число, помещаем его в стек
            stack.push(int(token))
        elif token in operators:
            # Если токен - оператор, извлекаем два числа из стека
            try:
                right_operand = stack.pop()
                left_operand = stack.pop()
                result = operators[token](left_operand, right_operand)
                stack.push(result)
            except IndexError:
                return "Ошибка: недостаточно операторов."
        else:
            return f"Ошибка: некорректный токен '{token}'."

    if stack.isEmpty():
        return "Ошибка: пустой стек, выражение некорректно."

    return stack.pop()

# Пример использования
expression = "3 4 + 2 * 7 /"
result = evaluate_postfix(expression)
print(f"Результат выражения '{expression}': {result}")

# Проверка некорректных выражений
invalid_expression = "3 4 + +"
result_invalid = evaluate_postfix(invalid_expression)
print(f"Результат некорректного выражения '{invalid_expression}': {result_invalid}")