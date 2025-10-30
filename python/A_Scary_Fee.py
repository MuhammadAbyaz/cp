import math

x, y = map(int, input().split())
print(math.ceil((x * 1000) / (1000 + y) - ((x * 1000) / (1000 + y) % 1000)))
