numOfStudents = int(input())

name = input()
highestScore = float(input())

for i in range(numOfStudents - 1):
    tempName = input()
    tempScore = float(input())
    if tempScore > highestScore:
        name = tempName
        score = tempScore

print(name, highestScore)