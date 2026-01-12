names = ["Me", "Lia", "Jake"]
stepr = []
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
for i in steps:
    print(names[steps.index(i)] + ":", i)
print("Total steps:")
for i in steps:
    print(names[steps.index(i)] + ":", sum(i))
    stepr.append(sum(i))
print(names[stepr.index(max(stepr))], "has the highest number of total steps at", max(stepr), "steps.")
print("The difference between the highest and lowest total steps is", max(stepr) - min(stepr))