sum = 0
num = int(input("Insert amount of numbers: "))
for i in range(1, num+1):
    number = int(input(f'Insert {i} number: '))
    sum += number

print(sum)