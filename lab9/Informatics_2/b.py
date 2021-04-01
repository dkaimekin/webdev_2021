year = int(input("insert year: "))

def is_leap(number):
    if number % 4 == 0: print("YES")
    else: print("NO")

is_leap(year)