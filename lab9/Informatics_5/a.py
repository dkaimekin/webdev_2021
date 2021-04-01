amt = int(input("Insert amount of numbers: "))
numbers = input()
numbers = numbers.split()
for i in range(0, amt, 2):
    print(numbers[i], end=" ")