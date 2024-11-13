def move_zero(my_list):
    count = 0

    for number in range(len(my_list)):
        if my_list[number] != 0:
            my_list[count] = my_list[number]
            count += 1

    while count < len(my_list):
        my_list[count] = 0
        count += 1

    return my_list

print(move_zero([0, 1, 0, 12, 3]))
print(move_zero([0]))
print(move_zero([1, 0, 13, 0, 0, 0, 5]))
print(move_zero([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))