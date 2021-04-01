amt = int(input("Insert amount of numbers: "))
numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)
pos_amt = 0
for i in range(0, amt):
    if numbers[i] > 0:
        pos_amt += 1

print(pos_amt)
