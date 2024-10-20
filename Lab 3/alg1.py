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

    def size(self):
        """Возвращает количество элементов в списке"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        """Ищет элемент в списке"""
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

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

    def append(self, item):
        """Добавляет новый элемент в конец списка"""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        """Возвращает индекс элемента в списке"""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} is not in list")

    def insert(self, pos, item):
        """Вставляет элемент в заданную позицию"""
        if pos < 0 or pos > self.size():
            raise IndexError("Index out of range")
        
        new_node = Node(item)
        if pos == 0:  # Вставка в начало
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.next
                index += 1
            new_node.next = current
            previous.next = new_node

    def pop(self, pos=None):
        """Удаляет и возвращает элемент по позиции.\n
        Если позиция не указана, удаляет последний элемент."""
        if self.is_empty():
            raise IndexError("pop from empty list")
        
        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError("Index out of range")

        current = self.head
        previous = None
        index = 0

        if pos == 0:  # Удаление из начала
            self.head = current.next
            return current.data
        else:
            while index < pos:
                previous = current
                current = current.next
                index += 1
            previous.next = current.next
            return current.data

    def __str__(self):
        """Возвращает строковое представление списка в Python-стиле"""
        result = []
        current = self.head
        while current is not None:
            result.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(result) + "]"

    def slice(self, start, stop):
        """Возвращает срез списка (копию), начиная с позиции start и заканчивая stop (не включая)"""
        if start < 0 or stop > self.size() or start >= stop:
            raise IndexError("Invalid start or stop index")

        sliced_list = UnorderedList()
        current = self.head
        index = 0

        while current is not None and index < stop:
            if index >= start:
                sliced_list.append(current.data)
            current = current.next
            index += 1

        return sliced_list


# Тестирование класса UnorderedList
if __name__ == "__main__":
    ul = UnorderedList()

    # Тесты метода add()
    ul.add(31)
    ul.add(77)
    ul.add(17)
    ul.add(93)
    ul.add(26)
    ul.add(54)

    print("Initial list:", ul)  # Должно напечатать список в обратном порядке добавления

    # Тесты метода append()
    ul.append(100)
    print("After append:", ul)

    # Тесты метода index()
    print("Index of 93:", ul.index(93))  # Должно быть 2
    try:
        print("Index of 999:", ul.index(999))  # Должен выдать ошибку
    except ValueError as e:
        print(e)

    # Тесты метода insert()
    ul.insert(2, 88)
    print("After insert:", ul)

    # Тесты метода pop()
    print("Popped item:", ul.pop())  # Должен удалить последний элемент
    print("After pop:", ul)
    print("Popped item at position 1:", ul.pop(1))  # Должен удалить элемент на позиции 1
    print("After pop at position 1:", ul)

    # Тесты метода slice()
    sliced = ul.slice(1, 4)
    print("Slice of list (1, 4):", sliced)
