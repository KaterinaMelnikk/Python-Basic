def calculator():

    while True:

        while True:
            try:
                first_number = float(input("Введіть перше число: "))
                break
            except ValueError:
                print("Це не є числом. Спробуйте ще раз.")


        while True:
            operation = input("Введіть дію (+, -, *, /): ")
            if operation not in ["+","-","*","/"]:
                print("Помилка: некоректна дія.")
                continue
            break

        while True:
            try:
                second_number = float(input("Введіть друге число: "))

                if operation == "/" and second_number == 0:
                    print("Помилка: ділення на нуль неможливе!")
                    answer = input("Якщо ви хочете ввести інше число, введіть 'yes': ")
                    if answer == "yes":
                        continue
                else: break
            except ValueError:
                print("Це не є числом. Спробуйте ще раз.")

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number

        print(f"Результат: {result}")

        answer = input("Якщо ви хочете продовжити, введіть 'yes': ")
        if answer.lower() != "yes":
            print("Вимкнення...")
            break

calculator()




