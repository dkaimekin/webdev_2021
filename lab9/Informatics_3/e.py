number = input()

def find_sum(number):
    sum = 0
    for i in range(0, len(number)):
        sum += int(number[i])
    return sum

print(find_sum(number))
