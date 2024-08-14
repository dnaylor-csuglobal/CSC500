"""
Write a Python program to find the addition and subtraction of two numbers.
Ask the user to input two numbers (num1 and num2). Given those two numbers,
add them together to find the output. Also, subtract the two numbers to find the output.
"""


def read_int():
    while True:
        try:
            return int(input())
        except:
            print("Input is not a valid number. Please try again: ")


print("Please input the first number: ")
num1 = read_int()
print("Please input the second number: ")
num2 = read_int()
print(f"The sum of {num1} and {num2} is {num1 + num2}")
print(f"The difference of {num1} and {num2} is {num1 - num2}")
