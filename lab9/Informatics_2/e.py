a = int(input("Insert number a: "))
b = int(input("Insert number b: "))

def find_bigger(a, b):
    if a > b: return 1
    elif a < b: return 2
    else: return 0


print(find_bigger(a, b))