number = int(input("Введіть 5-ти значне число: "))

d1 = number // 10000
d2 = (number // 1000) % 10
d3 = (number // 100) % 10
d4 = (number // 10) % 10
d5 = number % 10

reverse_number= (d5 * 10000) + (d4 * 1000) + (d3 * 100) + (d2 *10) + d1
print(reverse_number)