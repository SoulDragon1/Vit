def print_numbers():
    try:
        num = int(input("Введите число: "))
        if num < 1:
            print("Ошибка: число должно быть больше или равно 1.")
        else:
            for i in range(1, num + 1):
                print(i)
    except ValueError:
        print("Ошибка: введите корректное число.")


print_numbers()


def compare_numbers():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if num1 > num2:
            print(f"Большее число: {num1}")
        elif num2 > num1:
            print(f"Большее число: {num2}")
        else:
            print("Оба числа равны.")

    except ValueError:
        print("Ошибка: введите корректное число.")


compare_numbers()
