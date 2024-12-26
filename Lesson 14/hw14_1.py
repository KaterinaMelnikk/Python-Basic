class CustomException(Exception):
    pass

class Group_Limit_Error(CustomException):
    def __init__(self, message="Група не може містити більше 10 студентів!"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Номер залікової книжки: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # Додаємо студента до групи, якщо кількість не перевищує 10
        if len(self.group) >= 10:
            raise Group_Limit_Error()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
        else:
            print("Не вдалося знайти студента!")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group) if self.group else "Група порожня. Напевно, всі пішли на вихідні!"
        return f'Група номер: {self.number}\n{all_students}'


st1 = Student('Чоловік', 30, 'Тарас', 'Шевченко', 'UA001')
st2 = Student('Жінка', 25, 'Леся', 'Українка', 'UA002')
st3 = Student('Чоловік', 22, 'Іван', 'Франко', 'UA003')
st4 = Student('Жінка', 24, 'Ольга', 'Кобилянська', 'UA004')
st5 = Student('Чоловік', 23, 'Михайло', 'Коцюбинський', 'UA005')
st6 = Student('Жінка', 21, 'Марко', 'Вовчок', 'UA006')
st7 = Student('Чоловік', 26, 'Григорій', 'Сковорода', 'UA007')
st8 = Student('Жінка', 22, 'Катерина', 'Білокур', 'UA008')
st9 = Student('Чоловік', 28, 'Юрій', 'Яновський', 'UA009')
st10 = Student('Чоловік', 29, 'Олександр', 'Довженко', 'UA010')
st11 = Student('Чоловік', 27, 'Микола', 'Гоголь', 'UA011')

gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except Group_Limit_Error as e:
    print(f"Помилка: {e}")

print(gr)