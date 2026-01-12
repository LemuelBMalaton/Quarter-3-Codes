scores = [
    [95, 98, 91, 92, 85],
    [97, 90, 97, 91, 89],
    [94, 89, 90, 96, 84]
]
print("Scores of 5 students in 3 subjects")
for i in scores:
    print(i)
print("")
print("Average score for each subject")
for i in scores:
    print(sum(i)/len(i))