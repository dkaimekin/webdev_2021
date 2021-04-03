from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())


def print_string(number):
    for i in range(1, number + 1):
        print(str(i), end="")


print_string(n)