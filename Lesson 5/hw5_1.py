import keyword

def variable_name_checker(name):

    underscore = 0

    if keyword.iskeyword(name):
        return False

    if name[0].isdigit():
        return False

    for char in name:
        if char.isupper():
            return False
        elif not (char.isalnum() or char == "_"):
            return False
        if char == "_":
            underscore += 1
            if underscore > 1:
                return False
        else:
            underscore = 0

    return True

print(f"1. {variable_name_checker('_')}")                       #1
print(f"2. {variable_name_checker('__')}")                      #2
print(f"3. {variable_name_checker('___')}")                     #3
print(f"4. {variable_name_checker('x')}")                       #4
print(f"5. {variable_name_checker('get_value')}")               #5
print(f"6. {variable_name_checker('get value')}")               #6
print(f"7. {variable_name_checker('get!value')}")               #7
print(f"8. {variable_name_checker('some_super_puper_value')}")  #8
print(f"9. {variable_name_checker('Get_value')}")               #9
print(f"10. {variable_name_checker('get_Value')}")              #10
print(f"11. {variable_name_checker('getValue')}")               #11
print(f"12. {variable_name_checker('3m')}")                     #12
print(f"13. {variable_name_checker('m3')}")                     #13
print(f"14. {variable_name_checker('assert')}")                 #14
print(f"15. {variable_name_checker('assert_exception')}")       #15
