def split_my_list(my_list):
    if not my_list:
        return [[],[]]

    find_midpoint = (len(my_list) + 1) // 2

    first_half = my_list[:find_midpoint]
    second_half = my_list[find_midpoint:]

    return [first_half, second_half]

print(split_my_list([1, 2, 3, 4, 5, 6]))
print(split_my_list([1, 2, 3]))
print(split_my_list([1, 2, 3, 4, 5]))
print(split_my_list([1]))
print(split_my_list([]))