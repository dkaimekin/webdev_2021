number = int(input("insert number: "))
amt = 0
for i in range(1, number + 1):
    if number % i == 0:
        amt += 1

print(amt)