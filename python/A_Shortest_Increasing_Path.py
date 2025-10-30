t = int(input())
while t:
    t -= 1
    x, y = map(int, input().split())
    if x < y:
        print(2)
    elif x == y or y == 1:
        print(-1)
    else:
        if abs(x - y) == 1:
            print(-1)
        else:
            print(3)
