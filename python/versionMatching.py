def compareVersion(version1: str, version2: str) -> int:
    t1 = version1.split(".")
    t2 = version2.split(".")
    if len(t1) > len(t2):
        t2.extend(["0"] * (len(t1) - len(t2)))
    elif len(t2) > len(t1):
        t1.extend(["0"] * (len(t2) - len(t1)))
    t1 = int("".join(t1))
    t2 = int("".join(t2))
    if t1 < t2:
        return -1
    if t1 > t2:
        return 1
    return 0


print(compareVersion("1", "0"))
