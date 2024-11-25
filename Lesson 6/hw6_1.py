import string
def alfabet_range():

    letters = string.ascii_letters
    letters_reverse = string.ascii_letters[::-1]  # Зворотній рядок :)

    while True:
        firstletter_lastletter = input("Будь ласка, введіть дві літери через дефіс (a-Z): ")

        if "-" not in firstletter_lastletter or len(firstletter_lastletter.split("-")) != 2:
            print("Помилка: Введіть дві літери, розділені дефісом ('-').")
            continue

        first_letter, last_letter = firstletter_lastletter.split("-")

        if first_letter not in letters or last_letter not in letters:
            print("Помилка: Обидва символи мають бути літерами")
            continue

        first_index = letters.index(first_letter)
        last_index = letters.index(last_letter)

        if first_index <= last_index:
            return letters[first_index:last_index + 1]
        else:
            return letters_reverse[letters_reverse.index(first_letter):letters_reverse.index(last_letter) + 1]  # Зворотний порядок

print(alfabet_range())