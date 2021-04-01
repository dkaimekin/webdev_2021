a = int(input("insert first number: "))
b = int(input("insert second number: "))

def find_bigger(a, b):
    if a > b:
        return a
    else: return b

print(find_bigger(a, b))
