class HashTable:
    def __init__(self, size=11):
        self.size = size  # Starting size of the hash table
        self.table = [None] * self.size
        self.count = 0  # Number of key-value pairs in the table

    def hash(self, key):
        # Basic hash function to get the index
        return hash(key) % self.size

    def quadratic_probe(self, key):
        # Use quadratic probing to find an open slot
        index = self.hash(key)
        i = 1
        while self.table[index] is not None and self.table[index][0] != key:
            index = (self.hash(key) + i ** 2) % self.size
            i += 1
        return index

    def put(self, key, value):
        # Insert a key-value pair into the hash table
        if self.count / self.size > 0.7:  # Check if resizing is needed
            self.resize(self.next_prime(self.size * 2))
        
        index = self.quadratic_probe(key)
        if self.table[index] is None:
            self.count += 1
        self.table[index] = (key, value)

    def get(self, key):
        # Retrieve value associated with the key
        index = self.quadratic_probe(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def __delitem__(self, key):
        # Delete a key-value pair from the hash table
        index = self.quadratic_probe(key)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = None
            self.count -= 1
            if self.count / self.size < 0.2:  # Check if downsize is needed
                new_size = max(11, self.next_prime(self.size // 2))
                self.resize(new_size)

    def __len__(self):
        # Return the number of key-value pairs
        return self.count

    def __contains__(self, key):
        # Check if key is in the hash table
        return self.get(key) is not None

    def resize(self, new_size):
        # Resize the hash table to a new size (must be a prime number)
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0  # Reset count and reinsert items
        
        for item in old_table:
            if item is not None:
                self.put(item[0], item[1])

    def next_prime(self, n):
        # Find the next prime number greater than or equal to n
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

# Создание хэш-таблицы
ht = HashTable()

#nТестирование метода put и get
print("Добавление и получение элементов")
ht.put("apple", 100)
ht.put("banana", 200)
ht.put("orange", 300)

print(ht.get("apple"))   # Ожидается 100
print(ht.get("banana"))  # Ожидается 200
print(ht.get("orange"))  # Ожидается 300
print(ht.get("grape"))   # Ожидается None

print("\nПроверка оператора in")
print("apple" in ht)   # Ожидается True
print("grape" in ht)   # Ожидается False

print("\nПроверка оператора len")
print(len(ht))  # Ожидается 3

print("\nТест автоматического увеличения размера")
for i in range(8):
    ht.put(f"key{i}", i * 100)
print(len(ht))  # ожидается 11
print(ht.size)  # Проверим, что размер увеличился

print("\nТест удаления элементов")
del ht["banana"]
del ht["apple"]
del ht["orange"]
del ht["key0"]
del ht["key1"]
del ht["key2"]
del ht["key3"]
print("banana" in ht)  # Ожидается False
print(len(ht))         # Ожидается меньшее количество элементов

print(ht.size)         # Ожидается, что размер уменьшился
