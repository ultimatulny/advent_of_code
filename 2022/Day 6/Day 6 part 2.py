f = open('text.txt', 'r')
str = f.readline()
f.close()

for i in range(13, len(str),1):
    check = str[i-13] + str[i-12] + str[i-11] + str[i-10] + str[i-9] + str[i-8] + str[i-7] + str[i-6] + str[i- 5] + str[i-4] + str[i-3] + str[i-2] + str[i-1] + str[i]
    if len(set(check)) == 14:
        print(i + 1)
        break