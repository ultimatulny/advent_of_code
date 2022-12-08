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
muls = []

for i in range(1, len(forest) - 1, 1):
    for j in range(1, len(forest[i]) - 1, 1):
        local_i = i
        local_j = j
        current = forest[i][j]
        current_mul = 1
        sum = 0

        # Top
        for a in range(local_i, 0, -1):
            if current > forest[local_i - 1][j]:
                sum += 1
                local_i -= 1
        if local_i >= 1:
            sum += 1


        local_i = i
        current_mul *= sum
        sum = 0

        #Bottom
        for a in range(local_i, len(forest) - 1, 1):
            if current > forest[local_i + 1][j]:
                sum += 1
                local_i += 1
        if local_i < len(forest) - 1:
            sum += 1


        current_mul *= sum
        sum = 0

        #Left
        for a in range(local_j, 0, -1):
            if current > forest[i][local_j - 1]:
                sum += 1
                local_j -= 1
        if local_j >= 1:
            sum += 1

        local_j = j
        current_mul *= sum
        sum = 0

        #Right
        for a in range(local_j, len(forest[i]) - 1, 1):
            if current > forest[i][local_j + 1]:
                sum += 1
                local_j += 1
        if local_j < len(forest[i]) - 1:
            sum += 1

        current_mul *= sum

        muls.append(current_mul)

print(max(muls))






