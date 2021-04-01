amt = int(input("Insert amount of numbers: "))
numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)
bigger_amt = 0

for i in range(1, amt-1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        bigger_amt += 1

print(bigger_amt)