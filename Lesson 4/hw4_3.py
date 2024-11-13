import random

rand_list = []
elements_amount = random.randint(3,10)
for i in range(elements_amount):
    rand_list.append(random.randint(0, 9))
print(rand_list)

new_list = [rand_list[0],rand_list[2],rand_list[-2]]

print(new_list)