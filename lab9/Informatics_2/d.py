number = int(input("insert number: "))

def sign(n):
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0


print(sign(number))