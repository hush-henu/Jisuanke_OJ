a, b = map(int, input().split())

if -1 <= a <= 1:
    if -1 <= b <= 1:
        print("yes")
    else:
        print("no")
else:
    print("no")

