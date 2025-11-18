t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for val in range(n):
        if a[val] > b[val]:
            smVal = b[val]
            a.insert(val, smVal)
            a.pop()
            cnt += 1
    print(cnt)
    t -= 1
