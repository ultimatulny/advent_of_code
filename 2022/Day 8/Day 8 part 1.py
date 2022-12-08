f = open('text.txt', 'r')
str = f.readlines()
forest = []

for line in str:
    line = line[:len(line)-1]
    forest.append(line)

f.close()

for i in range(len(forest)):
    for j in range(len(forest[i])):
        print(forest[i][j], end="")
    print()

sum_trees = (len(forest) * 2) + ((len(forest[0]) - 2) * 2)

print(sum_trees)
for i in range(1, len(forest) - 1, 1):
    for j in range(1, len(forest[i]) - 1, 1):
        flag = True

        for horizontal in range(len(forest[i])):
            if forest[i][horizontal] >= forest[i][j] and horizontal != j:
                flag = False
            if horizontal == j:
                if flag:
                    break
                else:
                    flag = True

        if not(flag):
            flag = True
            for vertical in range(len(forest)):
                if forest[vertical][j] >= forest[i][j] and vertical != i:
                    flag = False
                if vertical == i:
                    if flag:
                        break
                    else:
                        flag = True

        if flag:
            sum_trees += 1
            print(f"{i} {j}")

print(sum_trees)