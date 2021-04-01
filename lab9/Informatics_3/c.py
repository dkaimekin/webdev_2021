import math

a = int(input("Insert a: "))
b = int(input("Insert b: "))

def find_squares(a, b):
    root_a = int(math.ceil(math.sqrt(a)))
    root_b = int((math.sqrt(b)))
    for i in range(root_a, root_b+1):
        print(i * i, " ")

find_squares(a, b)

