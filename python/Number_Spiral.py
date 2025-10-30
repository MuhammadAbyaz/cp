t = int(input())
while t:
    t -= 1
    y, x = map(int, input().split())
    maxi = max(x, y)
    prev = pow((maxi - 1), 2)
    if maxi % 2 == 0:
        if x > y:
            print(prev + y)
        else:
            print((maxi * maxi) - x + 1)
    else:
        if x > y:
            print((maxi * maxi) - y + 1)
        else:
            print(prev + x)
