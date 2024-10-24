number = int(input("Введіть 4-х значне число: "))

d1 = number // 1000
d2 = (number // 100) % 10
d3 = (number // 10) % 10
d4 = number % 10

print(d1)
print(d2)
print(d3)
print(d4)