

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"  # added for this module
        self.item_price = 0.0
        self.item_quantity = 0

    # Note that I am intentionally deviating from your example here by adding 2 decimal places to the output.
    # The item price is a float, and so necessitates printing to that degree of accuracy.
    def print_item_cost(self):
        print(
            f"{self.item_name} {self.item_quantity} @ ${self.item_price:,.2f} = ${self.cost():,.2f}")

    # returns the cost of the item(s). As we shaLL see, this will be very handy.
    def cost(self):
        return self.item_price * self.item_quantity


class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        index = - 1
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                index = i
                break
        if index >= 0:  # we found a match!
            self.cart_items.pop(index)
        else:
            print("Item not found in cart. Nothing removed.")

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        return sum(map(lambda item: item.cost(), self.cart_items))

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {len(self.cart_items)}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():,.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

    def find_item_by_name(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
        return None


def print_menu(shopping_cart):
    choice = 'init'
    while choice != 'q':
        print("MENU")
        print("a - Add item to cart")
        print("r - remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option:")
        choice = input()
        match choice:
            case 'q':
                print("Goodbye!")
                return
            case 'a':
                item = ItemToPurchase()
                print("Enter item name:")
                item.item_name = input()
                if shopping_cart.find_item_by_name(item.item_name) is not None:
                    print("Item already exists!")
                    continue
                print("Enter item description:")
                item.item_description = input()
                print("Enter item price:")
                item.item_price = float(input())
                print("Enter item quantity:")
                item.item_quantity = int(input())
                shopping_cart.cart_items.append(item)
                print(f"Item {item.item_name} has been added to the cart")
            case 'r':
                print("Enter item name:")
                item_name = input()
                match = shopping_cart.find_item_by_name(item_name)
                if match is not None:
                    print(f"Removing item {item_name}")
                    shopping_cart.cart_items.remove(match)
                else:
                    print("Unknown item. Returning to main menu.")
            case 'c':
                print("Enter item name:")
                item_name = input()
                item = shopping_cart.find_item_by_name(item_name)
                if item is not None:
                    print("Enter item quantity:")
                    quantity = int(input())
                    print(f"Updating item {item_name} quantity to {quantity}")
                    item.item_quantity = quantity
                else:
                    print("Unknown item. Returning to main menu.")
            case 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                shopping_cart.print_descriptions()
            case 'o':
                print("OUTPUT SHOPPING CART")
                shopping_cart.print_total()
            case _:
                print("Unknown menu choice. Please try again")
        print("")  # create a space


# main program
shopping_cart = ShoppingCart()
shopping_cart.customer_name = "John Doe"
shopping_cart.current_date = "February 1, 2020"
print_menu(shopping_cart)

