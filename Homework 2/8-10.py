#David Bonilla
#CIS2348 Ratner
#PSID:1913106
name = input()
reverseName = ""
name = name.strip()
for c in range(len(name)):
    if(name[c] != ''):
        reverseName = name[c]+reverseName
if(name==reverseName):
        print(name,'is a palindrome')
else:
        print(name,'is not a palindrome')
