#David Bonilla
#CIS2348 Ratner
#PSID:1913106

# class ItemToPurchase
class ItemToPurchase:

    # defining the self attributes
    def __init__(self):

        # attributes with default values
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

        # defining the print the items
    def print_item_cost(self):

        # print name, quality and price
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity ))

# calling the main
if __name__ == "__main__":

    # print the item 1
    print("Item 1")

    # item 1 & 2
    Item1 = ItemToPurchase()
    Item2 = ItemToPurchase()

    # prompt and Read item1 details
    Item1.item_name = input("Enter the item name:\n")
    Item1.item_price = int(input("Enter the item price:\n"))
    Item1.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nItem 2")

    # prompt and Read item2 details
    Item2.item_name = input("Enter the item name:\n")
    Item2.item_price = int(input("Enter the item price:\n"))
    Item2.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nTOTAL COST")

    # print the item 1 & 2 details
    Item1.print_item_cost()
    Item2.print_item_cost()

    # calculate cost
    total = (Item1.item_price * Item1.item_quantity) + (Item2.item_price * Item2.item_quantity)

    # print the total cost
    print("\nTotal: $" + str(total))
