def add_one(some_list):
    number_str = "".join([str(element) for element in some_list])
    number_int = int(number_str) + 1
    result = list([int(digit) for digit in str(number_int)])
    #print(result) #Перевірка
    return result
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")