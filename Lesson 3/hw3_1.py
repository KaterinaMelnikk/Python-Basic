first_number = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")

if operation not in ["+","-","*","/"]:
    print("Помилка: некоректна дія.")

else:
    second_number = float(input("Введіть друге число: "))

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    else:
        if second_number == 0:
            print("Помилка: ділення на нуль неможливе!")
        else:
            result = first_number / second_number

    if operation in ["+", "-", "*"] or (operation == "/" and second_number != 0):
        print("Результат:", result)
