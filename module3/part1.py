"""
Part 1:
Write a program that calculates the total
amount of a meal purchased at a restaurant.
The program should ask the user to enter the
charge for the food and then calculate the
amounts with an 18 percent tip and 7 percent
sales tax.
Display each of these amounts and the total price.
"""

# constants
SALES_TAX_PERCENT = 7
SERVICE_CHARGE_PERCENT = 18


# function that collects a non-zero float from standard input
def read_non_negative_float():
    while True:
        try:
            value = float(input())
            if value < 0:
                raise ValueError
            return value
        except:
            print("Input must be a non-negative value. Please try again: ")


print("Please enter the dollar amount charge for food: ")
food_charge = round(read_non_negative_float(), 2)  # round value to two decimal places
print(f"Food Charge: ${food_charge:,.2f}")  # comma separated to 2 decimal places

# calculate the sales tax
sales_tax = round(SALES_TAX_PERCENT * food_charge / 100.00, 2)  # round value to two decimal places
print(f"Sales Tax: ${sales_tax:,.2f} ({SALES_TAX_PERCENT}%)")  # comma separated to 2 decimal places

# calculate the service charge
service_charge = round(SERVICE_CHARGE_PERCENT * (food_charge + sales_tax) / 100.00, 2) # round value to two decimal places
print(f"Gratuity: ${service_charge:,.2f} ({SERVICE_CHARGE_PERCENT}%)")  # comma separated to 2 decimal places

# calculate the final amount
total_charge = food_charge + sales_tax + service_charge
print(f"Total: ${total_charge:,.2f}")  # comma separated to 2 decimal places
