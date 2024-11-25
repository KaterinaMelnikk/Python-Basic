def multiply_digits():

    while True:
        number_input = input("Введіть ціле число: ")
        if not number_input.isdigit():
            print("Помилка: введіть ціле число.")
            continue
        number = int(number_input)
        break

    while number > 9:
        digits = tuple(int(digit) for digit in str(number))
        result = 1
        for digit in digits:
            result *= digit
        number = result

    print(f"Результат: {number}")

multiply_digits()