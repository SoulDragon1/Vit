def greet(name):
    if not isinstance(name, str):
        print("Ошибка: Имя должно быть строкой.")
        return

    name = name.strip()

    if not name:
        print("Ошибка: Имя не может быть пустым.")
        return
    elif not name.isalpha():
        print("Ошибка: Имя должно содержать только буквы.")
        return
    
    print(f"Привет, {name.capitalize()}!")

user_name = input("Введите ваше имя: ")
greet(user_name)


def square(number):
    try:
        number = float(number)
    except ValueError:
        print("Ошибка: Введите корректное число.")
        return
    
    result = number ** 2
    print(f"Квадрат числа {number} равен {result}")


user_input = input("Введите число: ")
square(user_input)


def max_of_two(x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Ошибка: Оба аргумента должны быть числами.")
        return
    
    if x > y:
        print(f"Большее число: {x}")
    elif y > x:
        print(f"Большее число: {y}")
    else:
        print("Оба числа равны.")

x_input = input("Введите первое число: ")
y_input = input("Введите второе число: ")
max_of_two(x_input, y_input)


def describe_person(name, age=30):
    if not isinstance(name, str):
        print("Ошибка: Имя должно быть строкой.")
        return
    
    name = name.strip()
    if not name or not name.isalpha():
        print("Ошибка: Имя не может быть пустым и должно содержать только буквы.")
        return

    try:
        age = int(age)
        if age <= 0:
            print("Ошибка: Возраст должен быть положительным числом.")
            return
    except ValueError:
        print("Ошибка: Возраст должен быть числом.")
        return

    print(f"Имя: {name.capitalize()}, Возраст: {age}")

name_input = input("Введите имя: ")
age_input = input("Введите возраст (по желанию): ")

if age_input:
    describe_person(name_input, age_input)
else:
    describe_person(name_input)


def is_prime(number):
    try:
        number = int(number)
    except ValueError:
        print("Ошибка: Введите целое число.")
        return False
    
    if number <= 1:
        print(f"{number} не является простым числом.")
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} не является простым числом.")
            return False

    print(f"{number} является простым числом.")
    return True

user_input = input("Введите число: ")
is_prime(user_input)