#David Bonilla
#CIS2348 Ratner
#PSID:1913106

num_calls = 0

#defining Partition 
def partition(ID, a, b):
    p = ID[b]
    i = a - 1
    #for loop elements
    for c in range(a, b):
        if ID[c] <= p:
            i += 1
            ID[i], ID[c] = ID[c], ID[i]
    ID[i+1], ID[b] = ID[b], ID[i+1]
    return i+1

#defining Quicksort if element a is less than b
def quicksort(ID, a, b):
    if a < b:
        p = partition(ID, a, b)
        quicksort(ID, a, p-1)
        quicksort(ID, p+1, b)


if __name__ == "__main__":

    #list container for ID inputs
    ID = []
    userID = input()

    #while loop to append input ID to ID list
    while userID != "-1":
        ID.append(userID)
        userID = input()

    #quicksort items in list
    quicksort(ID, 0, len(ID)-1)
    num_calls = int(2 * len(ID)-1)
    print(num_calls)

    #print list items
    for userID in ID:
        print(userID)
