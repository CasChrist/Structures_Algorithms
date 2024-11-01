class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        # Добавляет новый узел в начало списка
        node = Node(key, value)
        node.next = self.head
        self.head = node

    def find(self, key):
        # Поиск узла по ключу
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        # Удаляет узел по ключу
        current = self.head
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.key, current.value
            current = current.next

class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [UnorderedList() for _ in range(self.size)]
        self.count = 0

    def hash(self, key):
        # Проверка, что ключ является строкой
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        if self.table[index].find(key) is None:
            self.count += 1
        self.table[index].add(key, value)
        
        if self.count / self.size > 0.7:
            self.resize(self.next_prime(self.size * 2))

    def get(self, key):
        index = self.hash(key)
        return self.table[index].find(key)

    def __delitem__(self, key):
        index = self.hash(key)
        if self.table[index].remove(key):
            self.count -= 1
            if self.count / self.size < 0.2:
                new_size = max(11, self.next_prime(self.size // 2))
                self.resize(new_size)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self.get(key) is not None

    def resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [UnorderedList() for _ in range(self.size)]
        self.count = 0
        
        for slot in old_table:
            for key, value in slot:
                self.put(key, value)

    def next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

def word_occurrence_order(text, hash_table):
    words = text.split()
    result = []
    for word in words:
        # Получаем текущий счётчик вхождений слова
        count = hash_table.get(word)
        
        if count is None:
            # Если слово встречается впервые, добавляем его со счётчиком 1
            hash_table.put(word, 1)
            result.append(1)
        else:
            # Увеличиваем счётчик и записываем обновлённое значение в таблицу
            count += 1
            hash_table.put(word, count)
            result.append(count)
    
    return result

ht = HashTable()

text = "Раз раз раз как меня слышно Повторяю раз раз раз Повторяю"

print(" ".join(map(str, word_occurrence_order(text, ht))))