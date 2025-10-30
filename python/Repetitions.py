dna = input()
p1 = 0
p2 = 0
maxRep = 1
while p2 < len(dna):
    if dna[p1] != dna[p2]:
        maxRep = max(maxRep, (p2 - p1))
        p1 = p2
    p2 += 1
maxRep = max(maxRep, (p2 - p1))
print(maxRep)
