numbers = input()
numbers = numbers.split()
mapped_numbers = map(float, numbers)
numbers = list(mapped_numbers)

def find_power(a, b):
    return a ** b

print(find_power(numbers[0], numbers[1]))
