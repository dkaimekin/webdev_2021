numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)

def xor(a, b):
    if (a and not b) or (not a and b):
        return 1
    else: return 0


print(xor(numbers[0], numbers[1]))