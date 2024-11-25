def seconds_to_date():
    time_units = (60, 3600, 86400)  # (секунди в хвилині, секунди в годині, секунди в дні)

    def get_day_word(days):
        day_words = {1: "день", "2-4": "дні", "other": "днів"}

        if days == 1:
            return day_words[1]
        elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
            return day_words["2-4"]
        else:
            return day_words["other"]

    while True:
        user_input = (input("Введіть кількість секунд (0-8639999): "))

        if not user_input.isdigit() or not (0 <= int(user_input) < 8640000):
            print("Помилка: введіть ціле число у діапазоні від 0 до 8639999.")
            continue

        seconds = int(user_input)

        days, remainder = divmod(seconds, time_units[2])
        hours, remainder = divmod(remainder,time_units[1])
        minutes, seconds = divmod(remainder,time_units[0])

        day_word = get_day_word(days)

        date = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(date)
        break

seconds_to_date()