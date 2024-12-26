def prime_generator(end):
    for i in range(2, end + 1):
        if all(i % n != 0 for n in range(2, int(i ** 0.5) + 1)):
            #Перевіряємо, чи немає дільників числа i у діапазоні від 2 до int(i ** 0.5) + 1
            #Якщо дільників немає, число є простим.
            yield i

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')