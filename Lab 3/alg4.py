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

# Тестирование стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Текущий стек после добавления:", stack.items)  # Ожидается: [3, 2, 1]
print("Верхний элемент стека:", stack.peek())  # Ожидается: 3
print("Размер стека:", stack.size())  # Ожидается: 3
print("Удаление элемента:", stack.pop())  # Ожидается: 3
print("Текущий стек после удаления:", stack.items)  # Ожидается: [2, 1]

class Queue:
    def __init__(self):
        """Инициализация очереди"""
        self.items = UnorderedList()

    def isEmpty(self):
        """Проверка на пустоту очереди"""
        return self.items.is_empty()

    def enqueue(self, item):
        """Добавление элемента в конец очереди"""
        self.items.append(item)  # В очереди элемент добавляется в конец

    def dequeue(self):
        """Удаление элемента из начала очереди"""
        if not self.isEmpty():
            return self.items.pop(0)  # Удаление первого элемента (начала очереди)
        else:
            raise IndexError("Попытка удаления из пустой очереди")

    def size(self):
        """Возвращает количество элементов в очереди"""
        return self.items.size()

# Тестирование очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Текущая очередь после добавления:", queue.items)  # Ожидается: [1, 2, 3]
print("Размер очереди:", queue.size())  # Ожидается: 3
print("Удаление первого элемента:", queue.dequeue())  # Ожидается: 1
print("Текущая очередь после удаления:", queue.items)  # Ожидается: [2, 3]

class Deque:
    def __init__(self):
        """Инициализация дека"""
        self.items = UnorderedList()

    def isEmpty(self):
        """Проверка на пустоту дека"""
        return self.items.is_empty()

    def addFront(self, item):
        """Добавление элемента в голову дека"""
        self.items.add(item)  # В начало списка (голова дека)

    def addRear(self, item):
        """Добавление элемента в хвост дека"""
        self.items.append(item)  # В конец списка (хвост дека)

    def removeFront(self):
        """Удаление первого элемента из дека"""
        if not self.isEmpty():
            return self.items.pop(0)  # Удаление первого элемента
        else:
            raise IndexError("Попытка удаления из пустого дека")

    def removeRear(self):
        """Удаление последнего элемента из дека"""
        if not self.isEmpty():
            return self.items.pop()  # Удаление последнего элемента
        else:
            raise IndexError("Попытка удаления из пустого дека")

    def size(self):
        """Возвращает количество элементов в деке"""
        return self.items.size()

# Тестирование дека
deque = Deque()
deque.addFront(1)
deque.addRear(2)
deque.addRear(3)
print("Текущий дек после добавления:", deque.items)  # Ожидается: [1, 2, 3]
print("Удаление первого элемента:", deque.removeFront())  # Ожидается: 1
print("Удаление последнего элемента:", deque.removeRear())  # Ожидается: 3
print("Текущий дек после удалений:", deque.items)  # Ожидается: [2]

import time

def test_performance(structure_class, operation, n=10000):
    """Тест производительности для структуры данных."""
    structure = structure_class()
    start_time = time.time()
    
    for i in range(n):
        operation(structure, i)
    
    end_time = time.time()
    return end_time - start_time

# Тестируем стек
def stack_push_test(stack, item):
    stack.push(item)

stack_time = test_performance(Stack, stack_push_test)
print(f"Время выполнения для стека: {stack_time} секунд")

# Тестируем очередь
def queue_enqueue_test(queue, item):
    queue.enqueue(item)

queue_time = test_performance(Queue, queue_enqueue_test)
print(f"Время выполнения для очереди: {queue_time} секунд")

# Тестируем дек
def deque_add_front_test(deque, item):
    deque.addFront(item)

deque_time = test_performance(Deque, deque_add_front_test)
print(f"Время выполнения для дека: {deque_time} секунд")
