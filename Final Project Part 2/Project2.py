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
 
item1 = item1[0],item1[5],item1[6],item1[3],item1[1]
item2 = item2[0],item2[5],item2[6],item2[3],item2[1]
item3 = item3[0],item3[5],item3[6],item3[3],item3[1]
item4 = item4[0],item4[5],item4[6],item4[3],item4[1]
item5 = item5[0],item5[5],item5[6],item5[3],item5[1]
item6 = item6[0],item6[5],item6[6],item6[1],item6[3],item6[7]
item7 = item7[0],item7[5],item7[6],item7[1],item7[3]

fullInventory = (item3, item2, item4, item7, item6, item1, item5)
print(fullInventory)

#list for all laptop items in inventory
laptopInventory = []

#for loop to check full inventory for laptop items
for x in fullInventory:
    if x[2] == "laptop":
        print('Laptop inventory:', x)

#list for all damaged items in inventory
damagedInventory = []

#for loop to check full inventory for past service items
for x in fullInventory:
    if x[4] == "5/27/2022":
        print('Past service date:', x)

#for loop to check full inventory damaged items
for x in fullInventory:
    if x[0] == "7346234":
        print('Damaged inventory:', x)

#list for all items past service date in inventory
pastServiceDateInventory = []

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
        if manufacturer in fullInventory and item in fullInventory:
            itemExist.append(fullInventory[x])
            print("Your item is:", itemExist )
        elif x == "damaged" or x == "5/27/2022":
            print("You may also want to consider", itemExist)
        elif manufacturer not in fullInventory or item not in fullInventory:
            print("No such item in inventory")
        
    #re-prompting the user with the option to quit
    manufacturer = str(input('Enter another manufacturer or press q to quit:'))
    item = str(input('Enter another item or press q to quit:'))
