#David Bonilla
#CIS2348 Ratner
#PSID:1913106
#input for the name
name = input()
reverseName = ""
name = name.strip()
#loop through the name to check for spaces
for c in range(len(name)):
    if(name[c] != ''):
        reverseName = name[c]+reverseName
#checks the character of name if the characters are the same
if(name==reverseName):
        print(name,'is a palindrome')
else:
        print(name,'is not a palindrome')
