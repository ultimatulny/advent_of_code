f = open('text.txt', 'r')
todo = []
for line in f:
    todo.append(line)
f.close()

field = []
for line in todo:
    if line == '\n':
        break
    field.append(line)

commands = []
flag = False
for line in todo:
    if line == '\n':
        flag = True
        continue
    if(flag):
        commands.append(line)

box = []
for j in range(1, len(field[0]), 4):
    tmp = []
    for i in range(len(field)):
        if field[i][j].isdigit():
            break
        if field[i][j] != ' ':
            tmp.append(field[i][j])
    tmp = tmp[::-1]
    box.append(tmp)


for i in range(len(commands)):
    command = commands[i].split()
    move = int(command[1])
    _from = int(command[3]) - 1
    to = int(command[5]) - 1

    readelems = []
    for a in range(move):
        tmp = box[_from].pop()
        readelems.append(tmp)

    readelems = readelems[::-1]
    for a in range(len(readelems)):
        box[to].append(readelems[a])


result = ''
for i in range(len(box)):
    result += box[i][-1]

print(result)