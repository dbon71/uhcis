#David Bonilla
#CIS2348 Ratner
#PSID:1913106
word = input()


password = ''

for character in word:

    if(character=='i'):
        password += '!'

    elif(character=='a'):
        password += '@'

    elif(character=='m'):
        password += 'M'

    elif(character=='B'):
        password += '8'

    elif(character=='o'):
        password += '.'

    else:
        password += character

print(password + 'q*s')
