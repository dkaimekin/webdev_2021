speed = int(input("Insert v: "))
time = int(input("Insert t: "))


def find_position(v, t):
    return (v * t) % 109


print(find_position(speed, time))
