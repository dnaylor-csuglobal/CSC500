import calendar


def read_int(min_value):
    while True:
        try:
            value = int(input())
            if value < min_value:
                raise Exception
            return value
        except:
            print("Not a valid input. Please try again: ")


rainfalls = []
print("Please enter the number of years:")
years = read_int(1)
for year in range(1, years + 1):
    print(f"Collecting rainfall for year {year} of {years}")
    for month in range(1, 13):
        print(f"Please enter the rainfall in inches for the month of {calendar.month_name[month]}:")
        monthly_rainfall = read_int(0)
        rainfalls.append(monthly_rainfall)
total_rainfall = sum(rainfalls)
average_rainfall = total_rainfall / len(rainfalls)
print(f"The total rainfall is {total_rainfall}")
print(f"The average rainfall is {average_rainfall}")
