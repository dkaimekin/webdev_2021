numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)


def find_smallest(numbers):
    largest = 10_000_000_000
    for element in numbers:
        if element < largest:
            largest = element
    return largest

print(find_smallest(numbers))