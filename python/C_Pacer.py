t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    requirements: list[list] = []
    maxCnt = 0
    for val in range(n):
        requirements.append(list(map(int, input().split())))

    for idx, req in enumerate(requirements):
        if idx == 0:
            distance = req[idx][0] - 0
        else:
            distance = req[idx - 1][0] - req[idx][0]
        if distance % 2 == 0 and req[idx][1] % 2 != 0:
            maxCnt += distance - 1
        elif distance % 2 == 0 and req[idx][1] % 2 == 0:
            maxCnt += distance
        elif distance % 2 != 0 and req[idx][1] % 2 != 0:
            maxCnt += distance
        else:
            maxCnt += distance - 1

    print(maxCnt)
