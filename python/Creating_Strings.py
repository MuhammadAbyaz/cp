from itertools import permutations

string = input()
perms = list(set(permutations(string, len(string))))
perms.sort()
print(len(perms))
for val in perms:
    print("".join(val))
