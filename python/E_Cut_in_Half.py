from collections import deque

t = int(input())
while t:
    t -= 1
    n, k, x = map(int, input().split())
    arr = deque(map(int, input().split()))
    arr = deque(sorted(arr))
    for i in range(k):
        val = arr.pop()
        arr.appendleft(val / 2)
        arr.appendleft(val / 2)
    print(f"{sorted(arr, reverse=True)[:x+1][-1]:.20f}")
