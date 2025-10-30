n, k = map(int, input().split())
odd = []
even = []
for val in range(n):
    if val % 2 == 0:
        even.append(val)
    else:
        odd.append(val)
odd.extend(even)
print(odd[k - 1])
