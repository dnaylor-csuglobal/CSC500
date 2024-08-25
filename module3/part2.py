def read_hour():
    while True:
        try:
            time = int(input())
            if not (0 <= time <= 23):
                raise ValueError

            return time
        except:
            print("Input is not a valid hour of the day. Please enter a number between 0 and 23 inclusive.")


def read_positive_int():
    while True:
        try:
            value = int(input())
            if value < 0:
                raise ValueError

            return value
        except:
            print("Input must be a positive integer. Please try again")


print("Please enter the current hour of the day (0-23):")
current_hour = read_hour()
print(f"You entered {current_hour}")
print("Please enter the number of hours to set the alarm:")
delay_hours = read_positive_int()
print(f"You entered {delay_hours}")
alarm_hour = (current_hour + delay_hours) % 24
print(f"The alarm is set for hour {alarm_hour}")
