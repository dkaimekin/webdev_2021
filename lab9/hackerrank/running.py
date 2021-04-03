if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    run = 0
    for element in arr:
        if element < arr[0]:
            run = element
            break
    print(run)