n = int(input("Insert number of pupils N: "))
k = int(input("Insert number of apples K: "))


def how_many_apples(n, k):
    return int((k - (k % n)) / n)


print(how_many_apples(n, k))