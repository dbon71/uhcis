#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#defining the class item to purchase
class ItemToPurchase:

    #defining self attributes
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    #defining item cost
    def print_item_cost(self):
        #print the output
        itemInfo= '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
        (self.item_quantity * self.item_price))
        itemCost = self.item_quantity * self.item_price
        return (itemInfo, itemCost)

    #defining item description
    def print_item_description(self):
        itemInfo = '{}: {}, %d oz.'.format(self.item_name, self.item_description, self.item_quantity)
        print(itemInfo)
        return(itemInfo)

#defining the class shopping cart
class ShoppingCart:

    #defining self attributes
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    #defining add item to cart
    def add_item(self):
        print('ADD ITEM TO CART')
        #input name/description of price, item and quantity
        item_name = str(input('Enter the item name:'))
        print()
        item_description = str(input('Enter the item description:'))
        print()
        item_price = int(input('Enter the item price:'))
        print()
        item_quantity = int(input('Enter the item quantity:'))
        print()

        #append items to list
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    #defining delete item for cart
    def remove_item(self):
        print('REMOVE ITEM FROM CART')

        #input the item to remove from the list
        itemInfo = str(input('Enter name of item to remove:'))
        print()
        a = 0

        #for loop to check all items in list
        for item in self.cart_items:
            #if item found, delete item in list
            if(item.item_name == itemInfo):
                del self.cart_items[a]
                #set value to true
                flag=True
                #break from the list
                break

            #set value to false
            else:
                flag=False
            a += 1

        #if item not found
        if(flag==False):
            #print the not found message
            print('Item not found in cart. Nothing removed.')

    #defining the change quantity
    def modify_item(self):
        print('CHANGE ITEM QUANTITY')

        #input item
        itemName = str(input('Enter the item name:'))
        print()

        #for loop to check all items in list
        for item in self.cart_items:
            #if item found, update the quantity in the list
            if(item.item_name == itemName):
                Quantity = int(input('Enter the new quantity:'))
                print()
                item.item_quantity = Quantity
                #set value to true
                flag=True
                #break from the list
                break

            #set value to false
            else:
                flag=False

        #if the item is not found
        if(flag==False):
            #print the item not found message
            print('Item not found in cart. Nothing modified.')
        print()

    #defining total items in the cart
    def get_num_items_in_cart(self):
        num_items=0
        #for loop to check items in list
        for item in self.cart_items:
            #add the items
            num_items= num_items+item.item_quantity

        #return the total of items
        return (num_items)

    #defining total cost of cart
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0

        #for loop to check items in list
        for item in self.cart_items:
            #mulitply the price and Quantity
            cost = (item.item_quantity * item.item_price)
            #add value to the Total_Cost
            total_cost += cost

        #return the value
        return (total_cost)

    #defining the total cost of cart
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    #defining the print item descriptions
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date),end='\n')
        print('\nItem Descriptions')

        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))

    #defining the output cart
    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        print()
        cart = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
              item.item_price, (item.item_quantity * item.item_price)))
            cart += (item.item_quantity * item.item_price)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()

        print('Total: ${}'.format(cart))

#defining the print menu
def print_menu(customer_Cart):

    #menu items
    menu = ('\nMENU\n'
    'a - Add item to cart\n'
    'r - Remove item from cart\n'
    'c - Change item quantity\n'
    'i - Output items\' descriptions\n'
    'o - Output shopping cart\n'
    'q - Quit\n')

    command = ''

    #while loop until user enters q
    while(command != 'q'):
        print(menu)

        #input command
        command = input('Choose an option:')
        print()

        #whileloop until user enters a,i,r,c,q commands
        while(command != 'a' and command != 'o' and command != 'i' and command != 'r'
              and command != 'c' and command != 'q'):
            command = input('Choose an option:')
            print()

        #command is a
        if(command == 'a'):
            customer_Cart.add_item()

        #command is o
        if(command == 'o'):
            customer_Cart.output_cart()

        #command is i
        if(command == 'i'):
            customer_Cart.print_descriptions()

        #command is r
        if(command == 'r'):
            customer_Cart.remove_item()

        #command is c
        if(command == 'c'):
            customer_Cart.modify_item()

def main():
    #input the customers name
    customer_name = str(input('Enter customer\'s name:'))
    print()

    #input date
    current_date = str(input('Enter today\'s date:'))
    print('\n')

    #print the name and date
    print('Customer name:', customer_name, end='\n')
    print('Today\'s date:', current_date, end='\n')

    #call the class
    newCart = ShoppingCart(customer_name, current_date)

    #print the details of the new cart
    print_menu(newCart)

if __name__ == '__main__':
    main()
