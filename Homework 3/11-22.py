#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#input of words
word = input().split()

#loop to print words and count frequency
for x in word:
    count = 0
    for y in word:
        if x == y:
            count += 1
    print(x, count)
