f = open('text.txt', 'r')

game = []
for line in f:
    line = line[:len(line)-1]
    game.append(line.split())
f.close()

score = 0
turns = [
    ['A', 'X'], # 0 Rock      X - Lose
    ['B', 'Y'], # 1 Paper     Y - Draw
    ['C', 'Z']  # 2 Scissors  Z - Win
]


for round in range(len(game)):
    botTurn = game[round][0]
    roundResult = game[round][1]
    botIndex = 0
    userIndex = 0

    for i in range(3):
        if botTurn == turns[i][0]:
            botIndex = i

    if roundResult == 'X':
        if botIndex == 0:
            userIndex = 2
        else:
            userIndex = botIndex - 1
    elif roundResult == 'Y':
        userIndex = botIndex
    elif roundResult == 'Z':
        if botIndex == 2:
            userIndex = 0
        else:
            userIndex = botIndex + 1

    score += userIndex + 1

    if botIndex == userIndex:
        score += 3
        continue
    elif botIndex == 2 and userIndex == 0:
        score += 6
        continue
    elif botIndex == 0 and userIndex == 2 or botIndex > userIndex:
        continue
    else:
        score += 6

print(score)