def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    return False


year = int(raw_input())
print
is_leap(year)