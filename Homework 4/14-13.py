#David Bonilla
#CIS2348 Ratner
#PSID:1913106

num_calls = 0

def partition(ID, a, b):
    p = ID[b]
    i = a - 1
    for c in range(a, b):
        if ID[c] <= p:
            i += 1
            ID[i], ID[c] = ID[c], ID[i]
    ID[i+1], ID[b] = ID[b], ID[i+1]
    return i+1

def quicksort(ID, a, b):
    if a < b:
        p = partition(ID, a, b)
        quicksort(ID, a, p-1)
        quicksort(ID, p+1, b)

if __name__ == "__main__":
    ID = []
    userID = input()
    while userID != "-1":
        ID.append(userID)
        userID = input()
    quicksort(ID, 0, len(ID)-1)
    num_calls = int(2 * len(ID)-1)
    print(num_calls)

    for userID in ID:
        print(userID)
