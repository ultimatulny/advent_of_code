f = open('text.txt', 'r')
lines = []
for line in f:
    line = line[:len(line)-1]
    lines.append(line)
f.close()

sums = []
sum = 0
for i in range(len(lines)):
    if(lines[i] == ''):
        sums.append(sum)
        sum = 0
    else:
        sum += int(lines[i])

sums.sort()
sum = 0
for i in range(3):
    sum += sums.pop()

print(sum)