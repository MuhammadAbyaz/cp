n = int(input())
arr = list(map(int, input().split()))
movs = 0
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        movs += abs(arr[i] - arr[i - 1])
        arr[i] = arr[i - 1]
print(movs)
