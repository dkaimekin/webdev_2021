import math


def find_c(a, b):
    c = math.sqrt(a**2 + b**2)
    return c


a = int(input("Insert a: "))

b = int(input("Insert b: "))

print(find_c(a, b))

