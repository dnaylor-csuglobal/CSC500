def read_float():
    while True:
        try:
            return float(input())
        except:
            print("Input is not a valid amount. Please try again: ")


print("Please enter the charge for food: ")
food_charge = round(read_float(), 2)
print(f"Food Charge: ${food_charge:,.2f}")
sales_tax = round(0.07 * food_charge, 2)
print(f"Sales Tax: ${sales_tax:,.2f} (7%)")
tip = round(0.18 * (food_charge + sales_tax), 2)
print(f"Tip: ${tip:,.2f} (18%)")
total_charge = food_charge + sales_tax + tip
print(f"Total: ${total_charge:,.2f}")
