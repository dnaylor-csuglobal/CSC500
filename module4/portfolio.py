def read_string(min_length):
    while True:
        try:
            value = input()
            if len(value) < min_length:
                raise Exception
            return value
        except:
            print(f"Input must be at least {min_length} characters. Please try again: ")


def read_int(min_value):
    while True:
        try:
            value = int(input())
            if value < min_value:
                raise Exception
            return value
        except:
            print(f"Input must be at least {min_value}. Please try again: ")


def read_float(min_value):
    while True:
        try:
            value = float(input())
            if value < min_value:
                raise Exception
            return value
        except:
            print(f"Input must be at least {min_value}. Please try again: ")


class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
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


# create a list up front. This allows the remainder of the code to be agnostic about the number of items we ask for.
# it will also allow us to avoid a lot of repeated code which is generally undesirable.
# Finally, it allows us to employ some powerful mapping techniques when we go to calculate the total cost.
items = [ItemToPurchase(), ItemToPurchase()]

# using enumerate allows us to iterate over the items and also get the index which we need to print the item number.
for index, item in enumerate(items):
    print(f"Item {index + 1}")  # one based
    print("Enter the item name:")
    item.item_name = read_string(1)  # at least one character
    print("Enter the item price:")
    # you could argue that the minimum allowed price and quantity should be greater than 0,
    # but the logic works even with 0, and it is the logical lower bound.
    item.item_price = read_float(0)
    print("Enter the item quantity:")
    item.item_quantity = read_int(0)

# print out the cost of each item. Here we can use a good ol' for loop
for item in items:
    item.print_item_cost()

# here we see that the decision to use a list is paying off since we can reduce a lot of looping code
# and concentrate on the business logic of generating the total cost
# To calculate the total cost, we simply need to "map" each item to its cost and then sum over all the costs.
# Python has a built-in map function for this purpose. We pass in the cost instance method,
# and the map function will apply the method to each item in the list
# This results in a list of floats which we then sum.
# This is an example of a "functional" programming technique,
# since we are iteratively applying a function to each element
total_cost = sum(map(ItemToPurchase.cost, items))

print(f"Total: ${total_cost:,.2f}")

