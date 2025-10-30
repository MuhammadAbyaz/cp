t = int(input())
flg = False
while t:
    t -= 1
    n = int(input())
    evens = []
    odds = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    arr = [0] * 2 * n
    evens = evens[::-1]
    for i in range(len(evens)):
        arr[i] = evens[i]
        arr[i + evens[i]] = evens[i]
    for i in range(2 * n):
        if arr[i] == 0:
            val = odds.pop()
            if val == 1:
                flg = True
                break
            arr[i] = val
            arr[i + val] = val
    if flg:
        for i in range(2 * n):
            if arr[i] == 0:
                arr[i] = 1
    print(*arr)
