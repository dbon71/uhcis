#David Bonilla
#CIS2348 Ratner
#PSID:1913106
#input for password
word = input()
password = ''

#loops to check if each character needs to be changed to a different element
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
#print method strengthens password
print(password + 'q*s')
