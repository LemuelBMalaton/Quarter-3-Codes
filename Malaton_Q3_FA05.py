days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steplist = []
dayrank = []
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
for i in range(5):
    steplist = []
    for j in range(3):
        steplist.append(steps[j][i])
    print(days[i] + ":", sum(steplist))
    dayrank.append(sum(steplist))
print("The most active day overall was", days[dayrank.index(max(dayrank))])