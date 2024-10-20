class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_iterative(head):
    """Итеративно разворачивает односвязный список."""
    previous = None
    current = head

    while current is not None:
        next_node = current.next  # Сохраняем указатель на следующий узел
        current.next = previous   # Разворачиваем указатель
        previous = current        # Переходим к следующему узлу
        current = next_node

    return previous  # /Новый первый узел после разворота

# Функция для создания списка из массива
def build_list(elements):
    head = None
    for element in reversed(elements):
        new_node = Node(element)
        new_node.next = head
        head = new_node
    return head

# Функция для печати списка
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Тест итеративного решения
if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print("Исходный список:")
    print_list(head)

    reversed_head = reverse_iterative(head)
    print("Развернутый список (итеративно):")
    print_list(reversed_head)

def reverse_recursive(head):
    """Рекурсивно разворачивает односвязный список."""
    if head is None or head.next is None:
        return head  # Базовый случай: список пуст или содержит один элемент

    new_head = reverse_recursive(head.next)  # Рекурсивно обращаем список начиная со второго узла

    head.next.next = head  # Разворачиваем указатель для текущего узла
    head.next = None       # Обнуляем следующий указатель, чтобы текущий узел стал последним

    return new_head  # Возвращаем новый первый узел

# Тест рекурсивного решения
if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print("Исходный список:")
    print_list(head)

    reversed_head = reverse_recursive(head)
    print("Развернутый список (рекурсивно):")
    print_list(reversed_head)
