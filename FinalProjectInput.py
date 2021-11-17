#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#importing the csv files
import csv
from operator import itemgetter

#list containers for each csv file
ManufacturerList=[]
PriceList=[]
ServDateList=[]

#Appending data information to the list containers of each file
#ManufacturerList information
with open("ManufacturerList.csv") as manufacList:
    manufacture = csv.reader(manufacList)
    for line in manufacture:
        ManufacturerList.append(line)

#PriceList information
with open("PriceList.csv") as priceList:
    price = csv.reader(priceList)
    for line in price:
        PriceList.append(line)

#ServiceDatesList information
with open("ServiceDatesList.csv") as servList:
    service = csv.reader(servList)
    for line in service:
        ServDateList.append(line)

#sort list by Order ID
new_manufac=(sorted(ManufacturerList, key=itemgetter(0)))
new_price=(sorted(PriceList, key=itemgetter(0)))
new_service=(sorted(ServDateList, key=itemgetter(0)))

#adding the prices and service dates to the full inventory list
for a in range(0,len(new_manufac)):
    new_manufac[a].append(PriceList[a][1])

for a in range(0,len(new_manufac)):
    new_manufac[a].append(ServDateList[a][1])

completeList = new_manufac

#formatting the full inventory
fullInventory = (sorted(completeList, key=itemgetter(1)))

#writing the a file for Full inventory from the list
with open('FullInventory.csv', 'w') as newFile:
    fullInventorywrite = csv.writer(newFile)

    for a in range(0, len(fullInventory)):
        fullInventorywrite.writerow(fullInventory[a])

#list containers for different item types
itemTypes = completeList
phoneList = []
laptopList = []
towerList = []

#search, organize, and append items into their correct list
for a in range(0, len(itemTypes)):
    if itemTypes[a][2] == "phone":
        phoneList.append(itemTypes[a])
    elif itemTypes[a][2] == "tower":
        towerList.append(itemTypes[a])
    elif itemTypes[a][2] == "laptop":
        laptopList.append(itemTypes[a])

#Writing a file for tower, phone, and laptop items
with open('LaptopInventory.csv', 'w') as newFile:
    laptopInventorywrite = csv.writer(newFile)

    for a in range(0, len(laptopList)):
        laptopInventorywrite.writerow(laptopList[a])

with open('PhoneInventory.csv', 'w') as newFile:
    phoneInventorywrite = csv.writer(newFile)

    for a in range(0, len(phoneList)):
        phoneInventorywrite.writerow(phoneList[a])

with open('TowerInventory.csv', 'w') as newFile:
    towerInventorywrite = csv.writer(newFile)

    for a in range(0, len(towerList)):
        towerInventorywrite.writerow(towerList[a])

#list container for damaged products
damagedList = []

#appending damaged items
for a in range(0, len(itemTypes)):
    if itemTypes[a][3] == "damaged":
        damagedList.append(itemTypes[a])

#formatting damaged items
damagedList = (sorted(damagedList, key=itemgetter(4), reverse=True))

#Writing a file for damaged products
with open('DamagedInventory.csv', 'w') as newFile:
    damagedInventorywrite = csv.writer(newFile)

    for a in range(0, len(damagedList)):
        damagedInventorywrite.writerow(damagedList[a])

#input for the user to list item manufacturer and type and container for item
inputManufacturer = str(input("Enter your manufacturer: "))
inputType = str(input("Please enter your item type: "))
userItem = []

#unless q is pressed to quit the program, continue
while(inputManufacturer != "q"):
    for a in range(0, len(completeList)):
        if inputManufacturer in completeList[a] and inputType in completeList[a]:
            userItem.append(completeList[a])

#if there was no input to list, product does not exist
    if len(userItem) != 0:
        userItem = sorted(userItem, key=itemgetter(4), reverse=True)
        print("Your item is: ", userItem[0])
    else:
        print("No such item in inventory")

    inputManufacturer = str(input("Enter your manufacturer, or q to exit query:"))
    inputType = str(input("Please enter your item type: "))
