f = open('text.txt', 'r')

sections = []
for line in f:
    line = line[:len(line)-1]
    sections.append(line)
f.close()

sum = 0
for i in range(len(sections)):
    section = sections[i].split(',')
    first = section[0].split('-')
    second = section[1].split('-')
    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        sum += 1
    elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        sum += 1

print(sum)