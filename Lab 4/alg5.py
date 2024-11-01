import hashlib
import secrets
import json
import os

# Файл для хранения данных пользователей
USER_DATA_FILE = "Lab 4/user_data.json"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f)

def hash_password(password, salt):
    return hashlib.scrypt(
        password.encode('utf-8'),
        salt=salt,
        n=16384, r=8, p=1,
        dklen=32
    )

def register(username, password):
    user_data = load_user_data()
    
    if username in user_data:
        print("Пользователь с таким логином уже существует.")
        return False

    # Генерация случайной соли длиной 32 байта
    salt = secrets.token_bytes(32)
    
    # Хэширование пароля с солью
    password_hash = hash_password(password, salt)

    # Сохранение данных пользователя
    user_data[username] = {
        "salt": salt.hex(),
        "password_hash": password_hash.hex()
    }
    save_user_data(user_data)
    print("Регистрация прошла успешно!")
    return True

def authenticate(username, password):
    user_data = load_user_data()
    
    if username not in user_data:
        print("Неверный логин или пароль.")
        return False

    salt = bytes.fromhex(user_data[username]["salt"])
    stored_password_hash = user_data[username]["password_hash"]

    # Хэшируем введённый пароль с полученной солью
    password_hash = hash_password(password, salt).hex()

    if password_hash == stored_password_hash:
        print("Авторизация успешна!")
        return True
    else:
        print("Неверный логин или пароль.")
        return False

if __name__ == "__main__":
    while True:
        action = input("Выберите действие: register или login (или exit для выхода): ").strip().lower()
        
        if action == "register":
            username = input("Введите логин: ").strip()
            password = input("Введите пароль: ").strip()
            register(username, password)
        
        elif action == "login":
            username = input("Введите логин: ").strip()
            password = input("Введите пароль: ").strip()
            authenticate(username, password)
        
        elif action == "exit":
            break
        else:
            print("Неверная команда.")
