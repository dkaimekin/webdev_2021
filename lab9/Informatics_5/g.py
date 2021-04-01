amt = int(input("Insert amount of numbers: "))
numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)

def reverse_array(numbers):
    reverse_index = int(len(numbers)/2)
    for i in range(0, reverse_index):
        numbers[i], numbers[len(numbers)-i-1] = numbers[len(numbers)-i-1], numbers[i]
    return numbers;

print(reverse_array(numbers))