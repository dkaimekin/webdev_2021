amt = int(input("Insert amount of numbers: "))
numbers = input()
numbers = numbers.split()
mapped_numbers = map(int, numbers)
numbers = list(mapped_numbers)
def find_same_signs(numbers):
    for i in range(1, amt):
        if numbers[i] > 0 and numbers[i-1] > 0:
            return "YES"
        elif numbers[i] < 0 and numbers[i-1] < 0:
            return "YES"
    return "NO"


print(find_same_signs(numbers))