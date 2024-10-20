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
    
def is_match(open_tag, close_tag):
    """Проверяет соответствие открывающего и закрывающего тегов."""
    return open_tag == close_tag[1:]

def extract_tags(html_string):
    """Извлекает теги из HTML строки."""
    tags = []
    i = 0
    while i < len(html_string):
        if html_string[i] == '<':
            j = i
            while j < len(html_string) and html_string[j] != '>':
                j += 1
            tags.append(html_string[i+1:j])  # Добавляем тег без угловых скобок
            i = j
        i += 1
    return tags

def check_html_balance(html_string):
    """Проверяет, сбалансированы ли теги в HTML-документе."""
    tags = extract_tags(html_string)
    stack = Stack()

    for tag in tags:
        if not tag.startswith('/'):  # Открывающий тег
            stack.push(tag)
        else:  # Закрывающий тег
            if stack.isEmpty():
                return False
            open_tag = stack.pop()
            if not is_match(open_tag, tag):
                return False

    # Если в конце стек пуст, все теги сбалансированы
    return stack.isEmpty()

# Пример использования
html_doc = "<html><head><title>Example</title></head><body><h1>Hello, world</h1></body></html>"

if check_html_balance(html_doc):
    print("HTML теги сбалансированы.")
else:
    print("HTML теги не сбалансированы.")