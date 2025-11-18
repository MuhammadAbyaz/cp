def zFunc(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            pi = i - l
            val = z[pi]
            if val < r - i + 1:
                z[i] = val
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z


s = input()
z = zFunc(s)
for i in range(len(s) - 1):
    if (z[i + 1] + i + 1) == len(s):
        print(i + 1, end=" ")
print(len(s))
