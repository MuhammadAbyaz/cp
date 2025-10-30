from collections import defaultdict, deque

n = int(input())
learnedSkillsCounter = 0
alreadyLearnedSkills = set()
skillTree: defaultdict[int, list[int]] = defaultdict(list)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    if a == 0:
        alreadyLearnedSkills.add(i)
        learnedSkillsCounter += 1
    else:
        skillTree[a].append(i)
        skillTree[b].append(i)

queue = deque(alreadyLearnedSkills)
while queue:
    skill = queue.popleft()
    for newSkill in skillTree[skill]:
        if newSkill not in alreadyLearnedSkills:
            learnedSkillsCounter += 1
            alreadyLearnedSkills.add(newSkill)
            queue.append(newSkill)

print(learnedSkillsCounter)
