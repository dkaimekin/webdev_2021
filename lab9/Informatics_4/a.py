import math
b = int(input("Insert b: "))

def find_squares(b):
    i = 1
    root_b = int((math.sqrt(b)))
    while i < root_b+1:
        print(i * i, end= " ")
        i += 1


find_squares(b)

