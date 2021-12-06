#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#import the files and datetime function for program execution

import datetime
import csv

#listing all items in manufacturer csv into a list

with open("ManufacturerList.csv", newline="") as File:
    rows = csv.reader(File, delimiter = ",")

    #manufacturer list container
    man = []

    #for loop to append all items
    for row in rows:
        man.append(row)

#listing all items in price csv into a list
with open("PriceList(1).csv", newline="") as File:
    rows = csv.reader(File, delimiter = ",")

    #price list container
    price = []

    #for loop to append all items
    for row in rows:
        price.append(row)

#listing all items in service csv into a list
with open("ServiceDatesList.csv", newline="") as File:
    rows = csv.reader(File, delimiter = ",")

    #service list container
    service = []

    #for loop to append all items
    for row in rows:
        service.append(row)

#list for all complete item elements
fullInventory = []

#appending all elements into full inventory
index=0
for x in range(0,len(man)):
    fullInventory.append(man[index])
    fullInventory.append(price[index])
    fullInventory.append(service[index])
    index = index+1

#sorting elements by ID, re-arragning list elements, arranging them in a list
fullInventory.sort()
item1 = fullInventory[0] + fullInventory[1]+ fullInventory[2]
item2 = fullInventory[3] + fullInventory[4]+ fullInventory[5]
item3 = fullInventory[6] + fullInventory[7]+ fullInventory[8]
item4 = fullInventory[9] + fullInventory[10]+ fullInventory[11]
item5 = fullInventory[12] + fullInventory[13]+ fullInventory[14]
item6 = fullInventory[15] + fullInventory[16]+ fullInventory[17]
item7 = fullInventory[18] + fullInventory[19]+ fullInventory[20]
fullInventory = [item3, item2, item4, item7, item6, item1, item5]
print(fullInventory)

#list for all laptop items in inventory
laptopInventory = []

#for loop to check full inventory for laptop items
for x in fullInventory:
    if x[6] == "laptop":
        print(x)

#list for all damaged items in inventory
damagedInventory = []

#for loop to check full inventory damaged items
for x in fullInventory:
    if x[0] == "7346234":
        print(x)

#list for all items past service date in inventory
pastServiceDateInventory = []

#for loop to check full inventory for past service items
for x in fullInventory:
    if x[3] == "5/27/2022":
        print(x)

#date time for the day and time program was executed
x = datetime.datetime.now()
print(x)

#input the user for manufacturer and item type
manufacturer = str(input('Who is your manufacturer:'))
item = str(input('What is your item:'))

itemExist =[] 

#while loop checking inventory if user hasn't quit
while manufacturer != "q":

    #for loop to check full inventory for items
    for x in fullInventory:

        #if and elif to check if item exists, doesn't exist, or suggesting an alternative
        if x == manufacturer or x == item or x != "damaged" and x != "5/27/2022":
            itemExist = fullInventory[x]
            print("Your item is:", fullInventory[x] )
        elif x != manufacturer or x != item:
            print("No such item in inventory")
        elif x == "damaged" or x == "5/27/2022":
            print("You may also want to consider", itemExist)

    #re-prompting the user with the option to quit
    manufacturer = str(input('Enter another manufacturer or press q to quit:'))
    item = str(input('Enter another item or press q to quit:'))
