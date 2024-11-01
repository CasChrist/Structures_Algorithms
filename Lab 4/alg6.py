import os
import hashlib

def calculate_file_hash(filepath):
    hash_sha256 = hashlib.sha256()
    
    # Читаем файл поблочно, чтобы не перегружать память для больших файлов
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    
    return hash_sha256.hexdigest()

def find_duplicates(directory_path):
    if not os.path.isdir(directory_path):
        print("Указанная директория не существует.")
        return
    
    hash_dict = {}
    duplicates = []

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Вычисляем хэш для текущего файла
            file_hash = calculate_file_hash(file_path)
            
            # Проверяем, есть ли уже файл с таким хэшем
            if file_hash in hash_dict:
                duplicates.append((file_path, hash_dict[file_hash]))
            else:
                hash_dict[file_hash] = file_path

    if duplicates:
        print("Найдены дубликаты:")
        for dup1, dup2 in duplicates:
            print(f"{dup1} <=> {dup2}")
    else:
        print("Дубликаты не найдены.")

if __name__ == "__main__":
    directory = input("Введите путь до директории: ").strip()
    find_duplicates(directory)
