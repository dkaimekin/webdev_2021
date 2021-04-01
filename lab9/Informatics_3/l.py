binary = input("Insert binary number: ")


def convert_to_decimal(number):
    decimal = 0
    binary = number[::-1]
    for i in range(0, len(binary)):
        if binary[i] == '1':
            decimal += 2**i
    return decimal

print(convert_to_decimal(binary))
