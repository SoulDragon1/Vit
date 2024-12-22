import hashlib
import uuid


class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password_hash = self._hash_password(password)
        self.user_id = str(uuid.uuid4())  # Генерация уникального идентификатора пользователя

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, new_password):
        self._password_hash = self._hash_password(new_password) # Устанавливает новый пароль.
        print("Пароль успешно изменён.")

    def check_password(self, password):
        return self._password_hash == self._hash_password(password)

    def identify(self):
        return f"Пользователь: {self.username}, ID: {self.user_id}"


# Интерактивный ввод данных от пользователя
if __name__ == "__main__":
    print("Создание нового аккаунта:")
    username = input("Введите имя пользователя: ")
    email = input("Введите электронную почту: ")
    password = input("Введите пароль: ")

    # Создаём объект пользователя
    user = UserAccount(username, email, password)
    print("\nАккаунт создан!")
    print(user.identify())  # Идентификация пользователя

    while True:
        print("\nМеню:")
        print("1. Проверить пароль")
        print("2. Сменить пароль")
        print("3. Показать данные пользователя")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            check_pass = input("Введите пароль для проверки: ")
            if user.check_password(check_pass):
                print("Пароль верен!")
            else:
                print("Пароль неверен!")
        elif choice == "2":
            new_pass = input("Введите новый пароль: ")
            user.set_password(new_pass)
        elif choice == "3":
            print(user.identify())
        elif choice == "4":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"



if __name__ == "__main__":
    # Создание объекта базового класса
    vehicle = Vehicle("АвтоВаз", "Лада")
    print(vehicle.get_info())  # Вывод: Марка: АвтоВаз, Модель: Лада

    # Создание объекта производного класса
    car = Car("УАЗ ", "УАЗ 452", "Бензин")
    print(car.get_info())  # Вывод: Марка: УАЗ, Модель: УАЗ 452, Тип топлива: Бензин
