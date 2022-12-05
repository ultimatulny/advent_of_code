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
for i in range(len(rucksacks)):
    countHalf = int(len(rucksacks[i][0]) / 2)
    first = rucksacks[i][0][:len(rucksacks[i][0])-countHalf]
    second = rucksacks[i][0][len(rucksacks[i][0])-countHalf:len(rucksacks[i][0])]

    for a in range(countHalf):
        if first[a] in second:
            sum += itemPriority(first[a])
            break

print(sum)