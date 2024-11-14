def even_index_calculator(my_list):

    if len(my_list) == 0:
        return 0

    sum_even_index = 0

    for even_index in range(0, len(my_list), 2):
        sum_even_index += my_list[even_index]

    multiply_by_last = sum_even_index * my_list[-1]

    return multiply_by_last

print(even_index_calculator([0, 1, 7, 2, 4, 8]))
print(even_index_calculator([1, 3, 5]))
print(even_index_calculator([6]))
print(even_index_calculator([]))