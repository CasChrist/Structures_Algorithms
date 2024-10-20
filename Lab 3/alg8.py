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

import random

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.success = random.random() < 0.7  # 70% вероятность успешной сдачи

    def __str__(self):
        result = "сдал" if self.success else "не сдал"
        return f"Студент {self.student_id}: {result}"

def simulate_exam_queue(students_count):
    queue = Queue()

    # Добавляем студентов в очередь
    for i in range(1, students_count + 1):
        student = Student(i)
        queue.enqueue(student)

    # Симуляция сдачи экзамена
    while not queue.isEmpty():
        current_student = queue.dequeue()  # Берем студента из очереди
        print(current_student)  # Печатаем результат сдачи

if __name__ == "__main__":
    simulate_exam_queue(10)  # Симуляция для 10 студентов
