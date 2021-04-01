a = int(input("Insert number a: "))
b = int(input("Insert number b: "))

def solution(a, b):
    if a != 1 and b != 1: print("YES")
    elif a == 1 and b == 1: print("YES")
    else: print("NO")


solution(a, b)