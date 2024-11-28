def common_elements():

    first_list = [element for element in range(101) if element % 3 == 0]
    second_list = [element for element in range(101) if element % 5 == 0]
    intersection_set = set(first_list).intersection(set(second_list))
    #print("Generated set:", intersection_set) #Перевірка
    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')