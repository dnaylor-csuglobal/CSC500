def read_int(min_value):
    while True:

        try:
            value = int(input())
            if value < min_value:
                raise Exception
            return value
        except:
            print("Not a valid input. Please try again: ")


# Collect the number of books purchased by the user
print("Please enter the number books you have purchased this month:")
number_books = read_int(0)
print(f"You have purchased {number_books} books this month.")


threshold_points = [(0, 0), (2, 5), (4, 15), (6, 30), (8, 60)]  # put the thresholds-point pairs in a single list
awarded = 0
for threshold, points in reversed(threshold_points):  # work backwards to calculate the points
    if number_books >= threshold:
        awarded = points
        break

print(f"You have been awarded {awarded} points")
