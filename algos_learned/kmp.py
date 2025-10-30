def lps(pattern):
    m = len(pattern)
    lps = [0] * m
    i = 1
    j = 0
    while i < m:
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    return lps


def kmp(haystack, needle):
    pos = []
    n, m = len(haystack), len(needle)
    lpsArr = lps(needle)
    i, j = 0
    while i < n:
        if haystack[i] == needle[i]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lpsArr[j - 1]
        if j == m:
            pos.append(i)
            j = lpsArr[j - 1]
    return pos
