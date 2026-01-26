scores = [
    [95, 98, 91, 92, 85],
    [97, 90, 97, 91, 89],
    [94, 89, 90, 96, 84]
]
print("Scores per student")
for i in range(3):
    print(scores[i])
print("Total score")
for i in range(3):
    print(sum(scores[i]))
print("Average score")
for i in range(3):
    print(sum(scores[i])/len(scores[i]))
highestscore = []
lowestscore = []
for i in range(3):
    highestscore.append(max(scores[i]))
print("Highest score:", max(highestscore))
for i in range(3):
    lowestscore.append(min(scores[i]))
print("Lowest score:", min(lowestscore))
