n, r = map(int, input().split())
doors = "".join(map(str, list(map(int, input().split()))))
sPos = doors.find("0")
lPos = doors.rfind("0")
cost = 0
if sPos == -1:
    print(0)
    exit()
if r >= sPos and r <= lPos + 1:
    for i in range(sPos, lPos + 1):
        if doors[i] == "0":
            cost += 1
        else:
            cost += 2
else:
    if r < sPos:
        for i in range(r, sPos):
            if doors[i] == "0":
                cost += 1
            else:
                cost += 2
        for i in range(sPos + 1, lPos + 1):
            if doors[i] == "0":
                cost += 1
            else:
                cost += 2
    elif r > lPos:
        for i in range(lPos, r):
            if doors[i] == "0":
                cost += 1
            else:
                cost += 2
        for i in range(sPos, lPos):
            if doors[i] == "0":
                cost += 1
            else:
                cost += 2


print(cost)
