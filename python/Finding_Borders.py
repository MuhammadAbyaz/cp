n = input()
N = len(n)
MOD = int(1e9) + 7
p1 = 31
p2 = 37
maxN = int(1e6) + 5

pow1 = [0] * maxN
pow2 = [0] * maxN

ph1 = ph2 = sh1 = sh2 = 0

pow1[0] = pow2[0] = 1
for i in range(1, N):
    pow1[i] = (pow1[i - 1] * p1) % MOD
    pow2[i] = (pow2[i - 1] * p2) % MOD

for i in range(N - 1):
    l = ord(n[i]) - ord("a") + 1
    r = ord(n[-i - 1]) - ord("a") + 1
    ph1 = (ph1 + l * pow1[i]) % MOD
    ph2 = (ph2 + l * pow2[i]) % MOD
    sh1 = (sh1 * p1 + r) % MOD
    sh2 = (sh2 * p2 + r) % MOD
    if ph1 == sh1 and ph2 == sh2:
        print(i + 1, end=" ")
