a = int(input("insert number a: "))
b = int(input("insert number b: "))

def find_even(a, b):
    if (a % 2 == 0):
        for i in range(a, b+1, 2):
            print(i, end=" ")
    else:
        for i in range(a+1, b+1, 2):
            print(i, end=" ")


find_even(a, b)