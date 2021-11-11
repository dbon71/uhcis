#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#input the user number
userInput = input()

#list container to check for pos-neg numbers
myList = [int(x) for x in userInput.split() if (int(x)>=0)]

#sorts number from least to greatest
myList.sort()

#print list
[print(x, end=' ') for x in myList]
