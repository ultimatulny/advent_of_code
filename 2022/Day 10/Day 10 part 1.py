f = open('text.txt', 'r')
str = f.readlines()
tic = 1
x = 1
cycles = []

for line in str:
    line = line[:len(line)-1]

    if line == 'noop':
        cycles.append(x * tic)
        tic += 1
    else:
        cmd = line.split()
        for i in range(2):
            if i == 0:
                cycles.append(x * tic)
                tic += 1
            else:
                cycles.append(x * tic)
                x += int(cmd[1])
                tic += 1
f.close()

sum = cycles[19] + cycles[59] + cycles[99] + cycles[139] + cycles[179] + cycles[219]
print(cycles)
print(f"Sum = {sum}")
