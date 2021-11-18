#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#defining list for descending order
def selection_sort_descend_trace(list):

    #for loop to sort items in list in descending order
    for a in range(len(list) - 1):
        m = a

        #nested for loop to check if the element is less than the placeholder
        for b in range(a + 1, len(list)):
            if list[m] < list[b]:
                m = b

        #switch element position
        list[a], list[m] = list[m], list[a]

        #for loop to print sorted output
        for data in list:
            print(data, end=' ')
        print()
    return list

#calling the function to sort list
if __name__ == '__main__':
    list = []
    list = [int(c) for c in input('').split()]
    selection_sort_descend_trace(list)
