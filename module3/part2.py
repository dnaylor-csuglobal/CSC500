"""
Part 2:
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13, and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem.
Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
"""


# read the hour between 0 and 24 inclusive from standard input with retry
def read_hour():
    while True:
        try:
            time = int(input())
            if not (0 <= time <= 23):
                raise ValueError

            return time
        except:
            print("Input is not a valid hour of the day. Please enter a number between 0 and 23 inclusive.")


# read a non-negative integer from standard input with retry
def read_non_negative_int():
    while True:
        try:
            value = int(input())
            if value < 0:
                raise ValueError

            return value
        except:
            print("Input must be a non-negative integer. Please try again")


print("Please enter the current hour of the day (0-23):")
current_hour = read_hour()
print(f"You entered {current_hour}")

print("Please enter the number of hours to set the alarm:")
delay_hours = read_non_negative_int()
print(f"You entered {delay_hours}")

alarm_hour = (current_hour + delay_hours) % 24  # modulo operator
alarm_days = (current_hour + delay_hours) // 24  # integer division
print(f"The alarm is set for hour {alarm_hour} in {alarm_days} days.")
