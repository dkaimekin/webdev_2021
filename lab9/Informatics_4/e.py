number = int(input("Insert number: "))

def find_power_of_two(number):
    temp = 1
    power = 0
    while temp < number:
        temp *= 2
        power += 1
    return power

print(find_power_of_two(number))