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

    def __str__(self):
        """Возвращает строковое представление списка"""
        result = []
        current = self.head
        while current is not None:
            result.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(result) + "]"


def move_to_front(n):
    """
    Читает строки с клавиатуры, сохраняет их в связном списке без повторов,
    реализует стратегию "сдвиг в начало"
    """
    ul = UnorderedList()

    for _ in range(n):
        user_input = input("Введите строку: ").strip()

        if ul.search(user_input):
            ul.remove(user_input)
        
        ul.add(user_input)
        
        print(f"Текущий список: {ul}")

# Пример использования
if __name__ == "__main__":
    n = int(input("Сколько строк вы хотите ввести? "))
    move_to_front(n)
