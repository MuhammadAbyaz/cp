t = int(input())
while t:
    t -= 1
    x, n = map(int, input().split())
    if n % 2 == 0:
        print(0)
    else:
        print(x)
