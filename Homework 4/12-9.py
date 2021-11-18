#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#input values for name and age
s = input().split()
firstName = s[0]
list = []

#while loop to check age error
while firstName != "-1":
    try:
        age=int(s[1])+1
    except ValueError:
        age=0

    #append to list
    list.append([firstName,age])

    #re-prompt input
    s=input().split()
    firstName = s[0]

#for loop to print out organized data
for name_age in list:
     print('{} {}'.format(name_age[0], name_age[1]))
