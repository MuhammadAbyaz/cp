def lps(pattern):
    m = len(pattern)
    lps = [0] * m
    prevLps, i = 0, 1
    while i < m:
        if pattern[i] == pattern[prevLps]:
            lps[i] = prevLps + 1
            prevLps += 1
            i += 1
        else:
            if prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps - 1]
    return lps


hay = input()
needle = input()
lpsArr = lps(needle)
n, m = len(hay), len(needle)
i = j = 0
cnt = 0
while i < n:
    if hay[i] == needle[j]:
        i += 1
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            j = lpsArr[j - 1]
    if j == m:
        cnt += 1
        j = lpsArr[j - 1]
print(cnt)
