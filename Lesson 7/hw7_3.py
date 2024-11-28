def second_index(text, some_str):

    index1 = text.find(some_str)
    if index1 != -1:
        index2 = text.find(some_str, index1 + 1)
        if index2 != -1 :
            #print(index2) ##Перевірка
            return index2
    return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
