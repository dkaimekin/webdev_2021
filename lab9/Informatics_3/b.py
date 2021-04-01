a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))
d = int(input("Insert d: "))

def find_numbers(a, b, c, d):
    for i in range(a, b+1):
        if i % d == c:
            print(i, end=" ")

find_numbers(a, b, c, d)