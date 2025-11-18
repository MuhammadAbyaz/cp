t = int(input())
while t:
    n, k = map(int, input().split())
    s = list(input())
    s.sort()
    res = ["+"] * n
    l = 0
    r = n - 1

    cnt = 0
    while cnt < k:
        if s[cnt] == "0":
            res[l] = "-"
            l += 1
        elif s[cnt] == "1":
            res[r] = "-"
            r -= 1
        else:
            if l == r:
                res[l] = "-"
            else:
                res[l] = "?"
                res[r] = "?"
                l += 1
        cnt += 1
    print("".join(res))

    t -= 1
