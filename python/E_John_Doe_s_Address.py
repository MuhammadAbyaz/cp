n, m = map(int, input().split())
colony = [[0 for _ in range(m)] for _ in range(n)]
pos = (0, 0)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        colony[i][j] = row[j]
        if row[j] == "A":
            pos = (i, j)
dir = [(-1, 0), (0, 1), (1, -1), (0, -1)]
