def z(s):
    n = len(s)    
    zArr = [0] * n
    l,r  = 0,0
    for i in range(1,n):
        if (i > r):
            l,r = i,i
            while(r<n and s[r] == s[r-l]):
                r+=1
            zArr[i] = r-l
            r-=1
        else:
            pi = i - l
            val =  zArr[pi]
            if (val < r - i + 1):
                zArr[i] = val
            else:
                l = i
                while (r < n and s[r] == s[r - l]):
                    r += 1
                zArr[i] = r - l
                r -= 1
    return zArr
