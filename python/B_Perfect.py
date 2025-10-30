from collections import defaultdict

n, m, k = map(int, input().split())
solvedProbs = defaultdict(list)
order = []
for _ in range(k):
    a, b = map(int, input().split())
    solvedProbs[a].append(b)
    if len(solvedProbs[a]) == m:
        order.append(a)
print(*order)
