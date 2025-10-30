n = int(input())
if n == 1:
    print(1)
elif n >= 2 and n <= 3:
    print("NO SOLUTION")
else:
    even = []
    odd = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if n != 4:
        even = even[::-1]
        odd = odd[::-1]
    even.extend(odd)
    print(*even)
