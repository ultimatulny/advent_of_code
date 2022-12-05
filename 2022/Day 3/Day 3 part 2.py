f = open('text.txt', 'r')

rucksacks = []
for line in f:
    line = line[:len(line)-1]
    rucksacks.append(line.split())
f.close()

def itemPriority(item):
    items = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    for i in range(len(items[0])):
        if item == items[0][i]:
            return i + 1


sum = 0
for i in range(0, len(rucksacks), 3):
    sumGroup = 0
    for badge in range(len(rucksacks[i][0])):
        if rucksacks[i][0][badge] in rucksacks[i + 1][0] and rucksacks[i][0][badge] in rucksacks[i + 2][0]:
            sumGroup = itemPriority(rucksacks[i][0][badge])
            break
    sum += sumGroup

print(sum)