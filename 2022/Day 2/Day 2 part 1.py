f = open('text.txt', 'r')

game = []
for line in f:
    line = line[:len(line)-1]
    game.append(line.split())
f.close()

score = 0
turns = [
    ['A', 'X'], # 0 Rock
    ['B', 'Y'], # 1 Paper
    ['C', 'Z']  # 2 Scissors
]


for round in range(len(game)):
    botTurn = game[round][0]
    userTurn = game[round][1]
    botIndex = 0
    userIndex = 0

    for i in range(3):
        if botTurn == turns[i][0]:
            botIndex = i
        if userTurn == turns[i][1]:
            userIndex = i
            score += i + 1

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