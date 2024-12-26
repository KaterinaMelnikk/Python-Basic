from student import Student
from group import Group
from exceptions import Group_Limit_Error

# Example usage
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

assert gr.find_student('Шевченко') == st1
assert gr.find_student('Шевченко2') is None


print(f"\n{'*'*50}\n")
gr.delete_student('Українка')
print(gr)