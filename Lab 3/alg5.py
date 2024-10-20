class Node:
		def __init__(self, data):
				self.data = data  # Данные узла
				self.next = None  # Ссылка на следующий узел
				self.prev = None  # Ссылка на предыдущий узел

class DoubleList:
		def __init__(self):
				self.head = None  # Голова списка
				self.tail = None  # Хвост списка

		def is_empty(self):
				"""Проверка, пуст ли список."""
				return self.head is None

		def size(self):
				"""Возвращает количество элементов в списке."""
				count = 0
				current = self.head
				while current is not None:
						count += 1
						current = current.next
				return count

		def search(self, item):
				"""Поиск элемента в списке."""
				current = self.head
				while current is not None:
						if current.data == item:
								return True
						current = current.next
				return False

		def add_to_front(self, item):
				"""Вставка элемента в начало списка."""
				new_node = Node(item)
				if self.is_empty():
						self.head = new_node
						self.tail = new_node
				else:
						new_node.next = self.head
						self.head.prev = new_node
						self.head = new_node

		def add_to_end(self, item):
				"""Вставка элемента в конец списка."""
				new_node = Node(item)
				if self.is_empty():
						self.head = new_node
						self.tail = new_node
				else:
						self.tail.next = new_node
						new_node.prev = self.tail
						self.tail = new_node

		def remove_from_front(self):
				"""Удаление элемента из начала списка."""
				if self.is_empty():
						raise IndexError("Удаление из пустого списка")
				if self.head == self.tail:  # В списке один элемент
						self.head = None
						self.tail = None
				else:
						self.head = self.head.next
						self.head.prev = None

		def remove_from_end(self):
				"""Удаление элемента из конца списка."""
				if self.is_empty():
						raise IndexError("Удаление из пустого списка")
				if self.head == self.tail:  # В списке один элемент
						self.head = None
						self.tail = None
				else:
						self.tail = self.tail.prev
						self.tail.next = None

		def insert_before(self, ref_node_data, item):
				"""Вставка элемента перед указанным узлом."""
				current = self.head
				while current is not None:
						if current.data == ref_node_data:
								new_node = Node(item)
								new_node.next = current
								new_node.prev = current.prev

								if current.prev is None:  # Вставляем перед первым элементом
										self.head = new_node
								else:
										current.prev.next = new_node
								current.prev = new_node
								return
						current = current.next
				raise ValueError(f"Узел с данными {ref_node_data} не найден")

		def insert_after(self, ref_node_data, item):
				"""Вставка элемента после указанного узла."""
				current = self.head
				while current is not None:
						if current.data == ref_node_data:
								new_node = Node(item)
								new_node.prev = current
								new_node.next = current.next

								if current.next is None:  # Вставляем после последнего элемента
										self.tail = new_node
								else:
										current.next.prev = new_node
								current.next = new_node
								return
						current = current.next
				raise ValueError(f"Узел с данными {ref_node_data} не найден")

		def remove_node(self, ref_node_data):
				"""Удаление указанного узла."""
				current = self.head
				while current is not None:
						if current.data == ref_node_data:
								if current.prev is None:  # Удаляем первый элемент
										self.head = current.next
								else:
										current.prev.next = current.next

								if current.next is None:  # Удаляем последний элемент
										self.tail = current.prev
								else:
										current.next.prev = current.prev
								return
						current = current.next
				raise ValueError(f"Узел с данными {ref_node_data} не найден")

		def __str__(self):
				"""Строковое представление списка."""
				result = []
				current = self.head
				while current is not None:
						result.append(str(current.data))
						current = current.next
				return "[" + ", ".join(result) + "]"

if __name__ == "__main__":
    dll = DoubleList()

    # Тест: вставка в начало
    dll.add_to_front(10)
    dll.add_to_front(20)
    print(dll)  # [20, 10]

    # Тест: вставка в конец
    dll.add_to_end(30)
    dll.add_to_end(40)
    print(dll)  # [20, 10, 30, 40]

    # Тест: размер списка
    print("Size:", dll.size())  # 4

    # Тест: поиск элемента
    print("Search 30:", dll.search(30))  # True
    print("Search 50:", dll.search(50))  # False

    # Тест: удаление из начала
    dll.remove_from_front()
    print(dll)  # [10, 30, 40]

    # Тест: удаление из конца
    dll.remove_from_end()
    print(dll)  # [10, 30]

    # Тест: вставка перед указанным узлом
    dll.insert_before(30, 25)
    print(dll)  # [10, 25, 30]

    # Тест: вставка после указанного узла
    dll.insert_after(25, 27)
    print(dll)  # [10, 25, 27, 30]

    # Тест: удаление указанного узла
    dll.remove_node(27)
    print(dll)  # [10, 25, 30]
