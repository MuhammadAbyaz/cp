n = int(input())
arr = []
for val in range(n):
    force = tuple(map(int, input().split()))
    arr.append(force)
xSum = 0
ySum = 0
zSum = 0
for val in arr:
    xSum += val[0]
    ySum += val[1]
    zSum += val[2]
if xSum == 0 and ySum == 0 and zSum == 0:
    print("YES")
else:
    print("NO")
