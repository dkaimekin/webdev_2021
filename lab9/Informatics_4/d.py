number = int(input("Insert number: "))

def is_power(number):
    if number == 1:
        print("YES")
    elif number < 1:
        print("NO")
    else:
        is_power(number/2)
    return 0;

is_power(number)