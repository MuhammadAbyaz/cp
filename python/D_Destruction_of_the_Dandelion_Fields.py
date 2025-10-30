t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    oddCount = 0
    evenCount = 0
    odd = []
    even = []
    ans = 0
    for val in arr:
        if val % 2 == 0:
            evenCount += 1
            even.append(val)
        else:
            oddCount += 1
            odd.append(val)
    if oddCount == 0:
        print(0)
        continue
    elif oddCount == 1:
        print(sum(arr))
        continue

    ans += sum(even)
    odd.sort()
    ans += odd.pop()
    odd.sort(reverse=True)
    ans += sum(odd[0 : (len(odd)) // 2])
    print(ans)
