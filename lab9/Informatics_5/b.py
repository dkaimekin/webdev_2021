amt = int(input("Insert amount of numbers: "))
numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)

for i in range(0, amt):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=" ")