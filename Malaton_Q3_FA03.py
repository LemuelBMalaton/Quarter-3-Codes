scores = [
    [95, 98, 91, 92, 85],
    [97, 90, 97, 91, 89],
    [94, 89, 90, 96, 84]
]
print("Scores of 5 students in 3 subjects")
for i in scores:
    print(i)
    
print("Total score of every student in each subject")
print(sum(scores[0]))
print(sum(scores[1]))
print(sum(scores[2]))


print("Average score for each subject")
for i in scores:
    print(sum(i)/len(i))
