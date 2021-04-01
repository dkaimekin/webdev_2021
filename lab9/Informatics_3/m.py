amt = int(input("Insert amount of numbers: "))
zero_amt = 0
for i in range(1, amt+1):
    number = int(input(f'Insert {i} number: '))
    if number == 0:
        zero_amt += 1

print(zero_amt)
