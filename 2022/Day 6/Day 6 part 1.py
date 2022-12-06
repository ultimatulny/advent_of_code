f = open('text.txt', 'r')
str = f.readline()
f.close()

for i in range(3, len(str),1):
    check = str[i-3] + str[i-2] + str[i-1] + str[i]
    if len(set(check)) == 4:
        print(i + 1)
        break